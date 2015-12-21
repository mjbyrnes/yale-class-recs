import math
import datetime
import time
import sqlite3 as lite
from django.db import models
from django.db.models import Q
from .models import Student, CourseProfile, CompleteData, YaleApiData
import operator

#Calculate workload score
def workload_score_calc(pref, actual): #int, int, boolean
  if actual <= pref:
    workload_score = 1
  else:
    w_diff = abs(actual - pref)
    workload_score = 1-math.log(w_diff+1, 3) #Same log base so that the rate of change is always the same. Chose 3 arbitrarily.

  return workload_score

#Calculate rating score
def rating_score_calc(pref, actual): #int, int, boolean
  r_diff = abs(actual - pref)

  if actual >= pref:
    rating_score = 1
  else:
    rating_score = 1-math.log(r_diff+1, 3) #Same log base so that the rate of change is always the same. Chose 3 arbitrarily.

  return rating_score

#Calculate subject score
def keyword_score_calc(terms, descrip): #array, string
  total_terms = len(terms)

  count = 0

  for i in terms:
    count = count + descrip.count(i)

  if count > total_terms:
    count = total_terms

  return count/total_terms

#Calculate class size score
def size_score_calc(seminar, size): #boolean, int
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
    size_score = 1

  if size_score < 0:
    size_score = 0

  return size_score

#Calculate overall score:
# Format of args:
# pref_work, pref_rat = int
# areas, skills = lists of strings with requirements
# search_terms = string of comma-separated search terms
# days = list of days of the week as abbreviations (M,T,W,Th,F)
# time = tuple of start and end time filters
# size = string which is either 'L' for lecture, 'S' for seminar, or 'E' for either
# major = a list of 1 string which is either '1' for in major, '0' for out of major, or '2' for neither
# weights = list of four preference weights: [difficulty, rating, size, time]
def match_score_calc(pref_work, pref_rat, areas, skills, search_terms, days, time, size, major, weights):
  # get all of the courses from the databases for current and historical courses
  courses = CompleteData.objects.all()
  old_courses = CompleteData.objects.all()

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
  pass #courses = courses.filter(time__iregex=r'') <-- use regex like this probably?

  # class size
  # should actually a function to provide score instead of a hard cutoff
  if size == 'L':
    courses.filter(num_students__gte=20) # filter out less than a certain size
  elif size == 'S':
    courses.filter(num_students__lte=30) # filter out greater than a certain size

  # major <-- need to incorporate the major of the individual
  if major[0] == '1':
    courses = courses.filter(subject='CPSC')
  elif major[0] == '0':
    courses = courses.exclude(subject='CPSC')

  # keywords <-- currently creates a list of scores but does not do anything with it
  keywords = [search_terms]
  word_scores = []
  for course in courses:
    x = keyword_score_calc(keywords, course.descrip)
    word_scores.append(x)
  #print scores

  scores = {}
  for course in courses:
    w_score = workload_score_calc(float(pref_work), course.average_difficulty)
    r_score = rating_score_calc(float(pref_rat), course.average_rating)
    s_score = size_score_calc(size, course.num_students)
    weighted_score = int(weights[0])*w_score + int(weights[1])*r_score + int(weights[2])*s_score
    scores[course.id] = weighted_score

    print str(w_score) + "+" + str(r_score) + "+" + str(s_score) + " = " + str(weighted_score)
  #print scores
  top10 = dict(sorted(scores.iteritems(), key=operator.itemgetter(1), reverse=True)[:10])
  for entry in top10:
    print CompleteData.objects.get(pk=entry).long_title
  print top10
  return courses

#AFTER CLICKING SUBMIT:

def recommend_classes():
  pass
  #get data from form
  #get data for all classes fitting the skills/areas/in major/time filters
  #run match_score_calc for each course
  #find 5 highest scores and present them with explanation


