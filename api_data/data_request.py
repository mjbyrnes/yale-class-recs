import urllib2 as u2
import sys
import json
import time
import sqlite3
try:
  import cPickle as pickle
except:
  import pickle

with open("course_subjects.json") as f:
  data = json.load(f)

subjects = []
for i in range(len(data)):
  subjects.append(data[i]["code"])

### get list of course subject codes from other JSON file generated by Course Subjects API
with open("course_dict") as f:
  data = pickle.load(f)

conn = sqlite3.connect('evaluations.sqlite', timeout=10)
c = conn.cursor()
# c.execute('SELECT * FROM {tn}'.\
# 	format(tn='yale_API_data'))
# test = c.fetchone()
# print test
max_len = []

for i in subjects:
	for j in xrange(len(data[i])):
		subj = i
		num = data[i][j]['courseNumber']
		shortTitle = data[i][j]['shortTitle']
		longTitle = data[i][j]['courseTitle']

		try:
			descrip = data[i][j]['description'].replace('<p>','').replace('</p>','')
		except AttributeError:
			descrip = ''

		times = data[i][j]['meetingPattern']
		try:
			times.remove('1 HTBA ')
		except ValueError:
			pass
		except AttributeError:
			pass
		try:
			time = times[0]
		except IndexError:
			time = ''

		dist_orig = data[i][j]['distDesg']
		dist = []
		for k in dist_orig:
			if k in ['YCWR', 'YCHU', 'YCQR', 'YCSO', 'YCSC', 'YCL1', 'YCL2', 'YCL3', 'YCL4', 'YCL5']:
				dist.append(k)

		max_len.append(len(dist))
		try:
			dist1 = dist[0]
		except IndexError:
			dist1 = ''
		try:
			dist2 = dist[1]
		except IndexError:
			dist2 = ''
		try:
			dist3 = dist[2]
		except IndexError:
			dist3 = ''

		c.execute("INSERT INTO 'yale_API_data' VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (subj, num, shortTitle, longTitle, descrip, time, dist1, dist2, dist3))

conn.commit()
c.close()
conn.close()


# print data["MATH"][0]["description"]
# print data["MATH"][0]["distDesg"]
# print data['MATH']
