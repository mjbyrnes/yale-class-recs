import math
import datetime as dt
import time
import sqlite3 as lite
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from .models import Student, CourseProfile, CompleteData, YaleApiData
import operator
import itertools

#Calculate workload score
def workload_score_calc(pref, actual, weight): #int, int, boolean
  if weight == 0:
    return 0
  if pref <= 2.5:
    if actual <= pref:
      workload_score = 1
    else:
      w_diff = abs(actual - pref)
      workload_score = 1-math.log(w_diff+1, 3) #Same log base so that the rate of change is always the same. Chose 3 arbitrarily.
  else:
    w_diff = abs(actual - pref)
    workload_score = 1-math.log(w_diff+1, 3)

  return workload_score*weight

#Calculate rating score
def rating_score_calc(pref, actual, weight): #int, int, boolean
  if weight == 0:
    return 0
  r_diff = abs(actual - pref)

  if actual >= pref:
    rating_score = 1
  else:
    rating_score = 1-math.log(r_diff+1, 3) #Same log base so that the rate of change is always the same. Chose 3 arbitrarily.

  return rating_score*weight

#Calculate subject score
def keyword_score_calc(terms, descrip): #array, string
  total_terms = len(terms)

  count = 0

  for i in terms:
    count = count + descrip.lower().count(i)

  if count > total_terms:
    count = total_terms

  return count*5

#Calculate class size score
def size_score_calc(seminar, size, weight): #boolean, int
  if weight == 0:
    return 0
  if seminar == "S":
    if size <= 25:
      size_score = 1
    else:
      size_score = 1-math.log(size-24,15)
  elif seminar == "L":
    if size >= 40:
      size_score = 1
    else:
      size_score = 1-math.log(41 - size,15)
  else:
    size_score = 0

  if size_score < 0:
    size_score = 0

  return size_score*weight

# parse database time
def time_parser(entry): #string
  if entry == '':
    return ''

  if entry[0] not in ['M', 'T', 'W', 'F']:
    return ''
  else:
    tm = entry.split(' ',1)[1]
    tm = tm.strip(' ')
    tm = tm.rstrip('p')

    start = tm.split('-')[0]
    end = tm.split('-')[1]
    start = [int(start.split('.')[0]), int(start.split('.')[1])]
    end = [int(end.split('.')[0]), int(end.split('.')[1])]

    if start[0] < 8:
      start[0] = start[0] + 12
      end[0] = end[0] + 12
    if end[0] < 9:
      end[0] = end[0] + 12

    start_time = dt.time(hour=start[0], minute=start[1])
    end_time = dt.time(hour=end[0], minute=end[1])

    cleaned_time = [start_time, end_time]
  return cleaned_time

#Calculate overall score:
# Format of args:
# pref_work, pref_rat = int
# areas, skills = lists of strings with requirements
# search_terms = string of comma-separated search terms
# days = list of days of the week as abbreviations (M,T,W,Th,F)
# time = tuple of start and end time filters
# size = string which is either 'L' for lecture, 'S' for seminar, or 'E' for either
# major = a list of 1 string which is either '1' for in major, '0' for out of major, or '2' for neither
# weights = list of three preference weights: [difficulty, rating, size]
# request = httprequest from the view to pass along user information
def match_score_calc(pref_work, pref_rat, areas, skills, search_terms, days, usertime, size, major, weights, request):
  # get all of the courses from the databases for current courses
  courses = CompleteData.objects.all()

  ### Filter Database using the following parameters: areas, skills, days, time, size, major ###
  # area and skills requirements
  for area in areas:
    courses = courses.filter(Q(dist1__contains=area) | Q(dist2__contains=area) | Q(dist3__contains=area))
  for skill in skills:
    courses = courses.filter(Q(dist1__contains=skill) | Q(dist2__contains=skill) | Q(dist3__contains=skill))

  # day of the week
  for weekday in days:
    courses = courses.exclude(time__contains=weekday)

  # time of day
  for course in courses:
    times = time_parser(course.time)
    # remove courses that start too early
    if times != '':
      if times[0] < usertime[0]:
        courses = courses.exclude(pk=course.id)
      # remove courses that start too late
      elif times[1] > usertime[1]:
        courses = courses.exclude(pk=course.id)

  # major <-- need to incorporate the major of the individual
  user_major = Student.objects.get(user=request.user).major
  if major[0] == '1':
    courses = courses.filter(subject='CPSC') # replace subject='CPSC' with subject__in=major_dict[user_major] once Raymond builds it
  elif major[0] == '0':
    courses = courses.exclude(subject='CPSC') 

  ### Keywords Preprocessing for preference weighting
  keywords = search_terms.strip().split(',')
  clean = []
  for word in keywords:
    clean.append(word.strip())

  ### Preference Weighting using the four required parameters
  scores = {}
  for course in courses:
    # workload
    w_score = workload_score_calc(float(pref_work), course.average_difficulty, int(weights[0]))
    # rating
    r_score = rating_score_calc(float(pref_rat), course.average_rating, int(weights[1]))
    # size
    s_score = size_score_calc(size, course.num_students, int(weights[2]))
    # time
    pass
    # keywords
    k_score = 2*keyword_score_calc(clean, course.longTitle)+keyword_score_calc(clean, course.descrip)

    # weight the scores according to user preference and store result in score dict
    weighted_score = int(weights[0])*w_score + int(weights[1])*r_score + int(weights[2])*s_score + k_score
    scores[course.id] = weighted_score

  ### Final Sorting Process to get top scores
  top50 = dict(sorted(scores.iteritems(), key=operator.itemgetter(1), reverse=True)[:50])
  # construct list to retrieve the top 50 or fewer courses
  ids = []
  for course_id in top50:
    ids.append(course_id)
  final = courses.filter(id__in=ids)
  return final
