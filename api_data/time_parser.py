#Code to transform times from database into time objects

def time_parser(entry): #string
	if entry == '':
		return ''

	#eliminate times that are "HTBA"
	if entry[0] not in ['M', 'T', 'W', 'F']:
		return ''
	else:
		#clean entry to just X.XX-Y.YY format
		tm = entry.split(' ',1)[1]
		tm = tm.strip(' ')
		tm = tm.rstrip('p')

		start = tm.split('-')[0]
		end = tm.split('-')[1]
		#Convert to integer
		start = [int(start.split('.')[0]), int(start.split('.')[1])]
		end = [int(end.split('.')[0]), int(end.split('.')[1])]

		#No classes start before 8 am. So if start time is before 8, must be PM. Add 12
		if start[0] < 8:
			start[0] = start[0] + 12
			end[0] = end[0] + 12
		if end[0] < 9:
			end[0] = end[0] + 12

		#Convert to datetime.time object
		start_time = datetime.time(hour=start[0], minute=start[1])
		end_time = datetime.time(hour=end[0], minute=end[1])

		cleaned_time = [start_time, end_time]
	print cleaned_time[0] < cleaned_time[1]
	#Return list of [start, end] time objects
	return cleaned_time

