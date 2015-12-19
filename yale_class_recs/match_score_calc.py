import math
import datetime
import time
import sqlite3 as lite

#Calculate workload score
def workload_score_calc(pref, actual): #int, int, boolean

	w_diff = abs(actual - pref)

	if actual <= pref:
		workload_score = 1
	else:
		workload_score = 1-log(w_diff+1, 3) #Same log base so that the rate of change is always the same. Chose 3 arbitrarily.

	return workload_score

# print(workload_score_calc(3,3.1,True))
# print(workload_score_calc(3,3.2,True))
# print(workload_score_calc(3,3.3,True))

#---------------------------------------------------------------------------------------------------------------

#Calculate rating score
def rating_score_calc(pref, actual): #int, int, boolean
	r_diff = abs(actual - pref)

	if actual >= pref:
		rating_score = 1
	else:
		rating_score = 1-log(r_diff+1, 3) #Same log base so that the rate of change is always the same. Chose 3 arbitrarily.

	return rating_score

# print(rating_score_calc(3,3.1,False))
# print(rating_score_calc(3,3.2,False))
# print(rating_score_calc(3,3.3,False))


#---------------------------------------------------------------------------------------------------------------

#Calculate subject score
def subject_score_calc(tags, descrip): #array, string
	total_terms = len(terms)

	count = 0

	for i in terms:
		count = count + descrip.count(i)

	if count > total_terms:
		count = total_terms

	return count/total_terms

#---------------------------------------------------------------------------------------------------------------

#Calculate class size score
def size_score_calc(seminar, size): #boolean, int
	if seminar:
		if size <= 25:
			size_score = 1
		else:
			size_score = 1-log(size-24,15)
	else:
		if size >= 40:
			size_score = 1
		else:
			size_score = 1-log(41 - size,15)

	if size_score < 0:
		size_score = 0

	return size_score

# print(size_score_calc(True, 45))
# print(size_score_calc(True, 15))
# print(size_score_calc(True, 26))
# print(size_score_calc(True, 27))

#---------------------------------------------------------------------------------------------------------------

#Calculate class time score
# def time_score_calc(start, end, intervals): #time, time, array of (start, end) tuples
# 	time_score = 0

# 	for i in intervals:
# 		if (start >= i[0]) & (end <= i[1]):
# 			time_score = 1
# 		elif (start >= i[0] - datetime.timedelta(minutes=30)) & (end <= i[1] + datetime.timedelta(minutes=30)):
# 			time_score = max(0.75, time_score)
# 		elif (start >= i[0] - datetime.timedelta(minutes=60)) & (end <= i[1] + datetime.timedelta(minutes=60)):
# 			time_score = max(0.5, time_score)
# 		elif (start >= i[0] - datetime.timedelta(minutes=90)) & (end <= i[1] + datetime.timedelta(minutes=90)):
# 			time_score = max(0.25, time_score)
# 		else:
# 			time_score = max(0, time_score)

# 	return time_score

# a = datetime.datetime(1,1,1,13,0,0)
# b = datetime.datetime(1,1,1,14,15,0)
# c = [(datetime.datetime(1,1,1,11,0,0),datetime.datetime(1,1,1,14,0,0)), (datetime.datetime(1,1,1,17,0,0),datetime.datetime(1,1,1,18,0,0))]

# print(time_score_calc(a, b, c))

#---------------------------------------------------------------------------------------------------------------

#Calculate overall score:
def match_score_calc(pref_work, pref_rat, search_terms, seminar, weights):
		
		#for each course, add new entry: match_score

#---------------------------------------------------------------------------------------------------------------

#AFTER CLICKING SUBMIT:

def recommend_classes():
	#get data from form
	#get data for all classes fitting the skills/areas/in major/time filters
	#run match_score_calc for each course
	#find 5 highest scores and present them with explanation






