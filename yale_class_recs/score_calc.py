import math
import datetime as dt
import time
import sqlite3 as lite
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from .models import Student, CompleteData
import operator
import itertools
try:
  import cPickle as cPickle
except:
  import pickle

# dict containing major to subject code relationships
major_dict = {'African American Studies (B.A.)': u'AFAM', 
'African Studies (B.A.)': ['AFST'],
'American Studies (B.A.)': ['AMST'],
'Anthropology (B.A.)': ['ANTH'],
'Applied Mathematics (B.A. or B.S.)': ['AMTH', 'MATH'],
'Applied Physics (B.S.)': ['APHY'],
'Archaeological Studies (B.A.)': ['ARCG'],
'Architecture (B.A.)': ['ARCH'],
'Art (B.A.)': ['ART'],
'Astronomy (B.A.)': ['ASTR'],
'Astronomy and Physics (B.S.)': ['ASTR', 'PHYS'],
'Astrophysics (B.S.)': ['ASTR', 'PHYS'],
'Biomedical Engineering (B.S.)': ['BENG'],
'Chemical Engineering (B.S.)': ['CENG'],
'Chemistry (B.A. or B.S.)': ['CHEM'],
'Classical Civilization (B.A.)': ['CLCV'],
'Classics (B.A.)': ['GREK', 'LATN', 'CLCV'],
'Cognitive Science (B.A. or B.S.)': ['CGSC'],
'Computer Science (B.A. or B.S.)': ['CPSC'],
'Computer Science and Mathematics (B.A. or B.S.)': ['CPSC', 'MATH'],
'Computer Science and Psychology (B.A.)': ['CPSC', 'PSYC'],
'Computing and the Arts (B.A.)': ['CPSC', 'CPAR'],
'East Asian Languages and Literatures (B.A.)': ['EALL', 'CHNS', 'JAPN', 'KREN'],
'East Asian Studies (B.A.)': ['EAST'],
'Ecology and Evolutionary Biology (B.A. or B.S.)': ['E&EB'],
'Economics (B.A.)': ['ECON'],
'Economics and Mathematics (B.A.)': ['ECON', 'MATH'],
'Electrical Engineering (B.S.)': ['EENG'],
'Electrical Engineering and Computer Science (B.S.)': ['EENG', 'CPSC'],
'Engineering Sciences (Chemical) (B.S.)': ['CENG'],
'Engineering Sciences (Electrical) (B.A. or B.S.)': ['EENG'],
'Engineering Sciences (Environmental) (B.A.)': ['ENVE'],
'Engineering Sciences (Mechanical) (B.A. or B.S.)': ['MENG'],
'English (B.A.)': ['ENGL'],
'Environmental Engineering (B.S.)': ['ENVE'],
'Environmental Studies (B.A.)': ['EVST'],
'Ethics, Politics, and Economics (B.A.)': ['EP&E'],
'Ethnicity, Race, and Migration (B.A.)': ['ER&M'],
'Film and Media Studies (B.A.)': ['FILM'],
'French (B.A.)': ['FREN'],
'Geology and Geophysics (B.S.)': ['G&G'],
'Geology and Natural Resources (B.A.)': ['G&G'],
'German (B.A.)': ['GMAN'],
'German Studies (B.A.)': ['GMAN'],
'Global Affairs (B.A.)': ['GLBL'],
'Greek: Ancient and Modern (B.A.)': ['GREK'],
'History (B.A.)': ['HIST'],
'History of Art (B.A.)': ['HSAR'],
'History of Science, Medicine, and Public Health (B.A.)': ['HSHM'],
'Humanities (B.A.)': ['HUMS'],
'Italian (B.A.)': ['ITAL'],
'Judaic Studies (B.A.)': ['JDST'],
'Latin American Studies (B.A.)': ['LATN'],
'Linguistics (B.A.)': ['LING'],
'Literature (B.A.)': ['LITR'],
'Mathematics (B.A. or B.S.)': ['MATH'],
'Mathematics and Philosophy (B.A.)': ['MATH', 'PHIL'],
'Mathematics and Physics (B.S.)': ['MATH', 'PHYS'],
'Mechanical Engineering (B.S.)': ['MENG'],
'Modern Middle East Studies (B.A.)': ['MMES', 'ARBC'],
'Molecular Biophysics and Biochemistry (B.A. or B.S.)': ['MB&B'],
'Molecular, Cellular, and Developmental Biology (B.A. or B.S.)': ['MCDB'],
'Music (B.A.)': ['MUSI'],
'Near Eastern Languages and Civilizations (B.A.)': ['NELC'],
'Philosophy (B.A.)': ['PHIL'],
'Physics (B.S.)': ['PHYS'],
'Physics and Geosciences (B.S.)': ['PHYS', 'G&G'],
'Physics and Philosophy (B.A.)': ['PHYS', 'PHIL'],
'Political Science (B.A.)': ['PLSC'],
'Portuguese (B.A.)': ['PORT'],
'Psychology (B.A. or B.S.)': ['PSYC'],
'Religious Studies (B.A.)': ['RLST'],
'Russian (B.A.)': ['RUSS'],
'Russian and East European Studies (B.A.)': ['RUSS', 'RSEE'],
'Sociology (B.A.)': ['SOCY'],
'South Asian Studies (second major only)': ['SAST'],
'Spanish (B.A.)': ['SPAN'],
'Special Divisional Major (B.A. or B.S.)': [],
'Statistics (B.A. or B.S.)': ['STAT'],
'Theater Studies (B.A.)': ['THST'],
'Women\'s, Gender, and Sexuality Studies (B.A.)': ['WGSS']}

#Calculate workload score
def workload_score_calc(pref, actual, weight): #int, int, boolean
  if weight == 0:
    return 0
  # consider student who don't care about heavy workload specifically
  if pref <= 2.5:
    if actual <= pref:
      workload_score = 1
    else:
      w_diff = abs(actual - pref)
      # use a logarithmic distribution to capture user's utility preferences
      workload_score = 1-math.log(w_diff+1, 3)
  # for students who care more about workload, 
  # score based on distance from target as opposed to whether it's below or not
  else:
    w_diff = abs(actual - pref)
    workload_score = 1-math.log(w_diff+1, 3)

  return workload_score

#Calculate rating score
def rating_score_calc(pref, actual, weight): #int, int, boolean
  if weight == 0:
    return 0
  r_diff = abs(actual - pref)
  # use a logarithmic distribution to capture user's utility preferences
  if actual >= pref:
    rating_score = 1
  else:
    rating_score = 1-math.log(r_diff+1, 3) 

  return rating_score

#Calculate subject score
def keyword_score_calc(terms, descrip): #array, string
  total_terms = len(terms)

  count = 0
  # count terms in description or title based on input
  for i in terms:
    count = count + descrip.lower().count(i)

  if count > total_terms:
    count = total_terms
  # return number of terms for scoring
  return count

#Calculate class size score
def size_score_calc(seminar, size, weight): #boolean, int
  # filter out completely if user does not care
  if weight == 0:
    return 0
  # score for seminar
  if seminar == "S":
    if size <= 25:
      size_score = 1
    else:
      size_score = 1-math.log(size-24,15)
  # score for lecture
  elif seminar == "L":
    if size >= 40:
      size_score = 1
    else:
      size_score = 1-math.log(41 - size,15)
  # score for either
  else:
    size_score = 0

  if size_score < 0:
    size_score = 0

  return size_score

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
    # split the expression into its parts
    start = tm.split('-')[0]
    end = tm.split('-')[1]
    start = [int(start.split('.')[0]), int(start.split('.')[1])]
    end = [int(end.split('.')[0]), int(end.split('.')[1])]
    # compare to make sure the times are all valid
    if start[0] < 8:
      start[0] = start[0] + 12
      end[0] = end[0] + 12
    if end[0] < 9:
      end[0] = end[0] + 12
    # create datetime objects
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

  # major 
  user_major = Student.objects.get(user=request.user).major
  if major[0] == '1':
    courses = courses.filter(subject__in=major_dict[user_major])
  elif major[0] == '0':
    courses = courses.exclude(subject__in=major_dict[user_major]) 

  ### Keywords Preprocessing for preference weighting
  keywords = search_terms.lower().strip().split(',')
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
    # keywords
    k_score = 2*keyword_score_calc(clean, course.longTitle)+keyword_score_calc(clean, course.descrip)

    # weight the scores according to user preference and store result in score dict
    weighted_score = int(weights[0])*w_score + int(weights[1])*r_score + int(weights[2])*s_score + int(weights[3])*k_score
    scores[course.id] = weighted_score

  ### Final Sorting Process to get top scores
  top50 = dict(sorted(scores.iteritems(), key=operator.itemgetter(1), reverse=True)[:100])
  # construct list to retrieve the top 50 or fewer courses
  ids = []
  #print sorted(top50.iteritems(), key=operator.itemgetter(1), reverse=True)
  for course_id in sorted(top50.iteritems(), key=operator.itemgetter(1), reverse=True):
    ids.append(course_id[0])

  # order the results properly to display them for the user
  final_courses = []
  for i_d in ids:
    final_courses.append(courses.filter(id=i_d)[0])

  return final_courses



