from .models import CompleteData
import random as r

def intro(title):
	intros = [
		"%s is a good fit for you. " % title,
		"We think you'd really enjoy %s. " % title,
		"Thanks for using Eli. %s would be a great match for you. " % title
	]

	i = r.randrange(0,len(intros))
	return intros[i]

def weighting(course, difficulty, rating, weights):
	e = ""
	if weights[0] > weights[1]:
		e += "You said that the difficulty of the course was important to you, "
		e += "and this course's difficulty rating of %s " % str(course.average_difficulty)
		e += "is close to your requested difficulty rating of %s. " % str(difficulty)
	elif weights[1] > weights[0]:
		e += "You said that the rating of the course was important to you, "
		e += "and this course's average rating of %s " % str(course.average_rating)
		e += "is close to your requested rating of %s. " % str(rating)
	else:
		e += "It looks like difficulty and rating are both equally important to you. "
		e += "This class has a good balance between these two factors, with "
		e += "an average difficulty of %s " % str(course.average_difficulty)
		e += "and an average rating of %s. " % str(course.average_rating)

	return e

def size_type(size):
	e = ""
	if size == 'E':
		e += "You also said you had no preference about the size of the class, so both "
		e += "lectures and seminars were considered in the search. "
	if size == 'S':
		e += "It's also a seminar, like you requested. "
	if size == 'L':
		e += "It's also a lecture course, like you requested. "
	return e

def time(start, end, day, weights):
	e = ""

	if int(weights[3]) == 5:
		e += "Since you told us the times you chose are a firm requirement, "
		e += "we only looked for courses within the time range you selected. "

	return e

def in_major(major, title):
	e = ""
	if int(major) == 0:
		e += "Finally, you said you wanted a class that's not in your major, which is "
		e += "true for %s. " % title
	elif int(major) == 1:
		e += "Finally, you said you wanted a class that is in your major, which is "
		e += "true for %s. " % title
	else:
		e += "Finally, you said you had no preference regarding whether or not the "
		e += "course is in your major, so we searched all available courses "
		e += "to find the best one for you. "

	return e

def explain(course, difficulty, rating, size, day, start_time,
    end_time, area, skills, keywords, major, weights):

	explanation = ""
	explanation += intro(course.longTitle)
	explanation += weighting(course, difficulty, rating, weights)
	explanation += size_type(size)
	explanation += time(start_time, end_time, day, weights)
	explanation += in_major(major, course.longTitle)

	return explanation