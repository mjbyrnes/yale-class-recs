#Models corresponding to database tables for the application
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import json

#Strings for each possible major
majors = ['African American Studies (B.A.)','African Studies (B.A.)','American Studies (B.A.)','Anthropology (B.A.)',
'Applied Mathematics (B.A. or B.S.)','Applied Physics (B.S.)','Archaeological Studies (B.A.)','Architecture (B.A.)',
'Art (B.A.)','Astronomy (B.A.)','Astronomy and Physics (B.S.)','Astrophysics (B.S.)','Biomedical Engineering (B.S.)',
'Chemical Engineering (B.S.)','Chemistry (B.A. or B.S.)','Classical Civilization (B.A.)','Classics (B.A.)',
'Cognitive Science (B.A. or B.S.)','Computer Science (B.A. or B.S.)','Computer Science and Mathematics (B.A. or B.S.)',
'Computer Science and Psychology (B.A.)','Computing and the Arts (B.A.)','East Asian Languages and Literatures (B.A.)',
'East Asian Studies (B.A.)','Ecology and Evolutionary Biology (B.A. or B.S.)','Economics (B.A.)','Economics and Mathematics (B.A.)',
'Electrical Engineering (B.S.)','Electrical Engineering and Computer Science (B.S.)','Engineering Sciences (Chemical) (B.S.)',
'Engineering Sciences (Electrical) (B.A. or B.S.)','Engineering Sciences (Environmental) (B.A.)',
'Engineering Sciences (Mechanical) (B.A. or B.S.)','English (B.A.)','Environmental Engineering (B.S.)',
'Environmental Studies (B.A.)','Ethics, Politics, and Economics (B.A.)','Ethnicity, Race, and Migration (B.A.)',
'Film and Media Studies (B.A.)','French (B.A.)','Geology and Geophysics (B.S.)','Geology and Natural Resources (B.A.)',
'German (B.A.)','German Studies (B.A.)','Global Affairs (B.A.)','Greek, Ancient and Modern (B.A.)','History (B.A.)',
'History of Art (B.A.)','History of Science, Medicine, and Public Health (B.A.)','Humanities (B.A.)','Italian (B.A.)',
'Judaic Studies (B.A.)','Latin American Studies (B.A.)','Linguistics (B.A.)','Literature (B.A.)','Mathematics (B.A. or B.S.)',
'Mathematics and Philosophy (B.A.)','Mathematics and Physics (B.S.)','Mechanical Engineering (B.S.)','Modern Middle East Studies (B.A.)',
'Molecular Biophysics and Biochemistry (B.A. or B.S.)','Molecular, Cellular, and Developmental Biology (B.A. or B.S.)',
'Music (B.A.)','Near Eastern Languages and Civilizations (B.A.)','Philosophy (B.A.)','Physics (B.S.)','Physics and Geosciences (B.S.)',
'Physics and Philosophy (B.A.)','Political Science (B.A.)','Portuguese (B.A.)','Psychology (B.A. or B.S.)','Religious Studies (B.A.)',
'Russian (B.A.)','Russian and East European Studies (B.A.)','Sociology (B.A.)','South Asian Studies (second major only)',
'Spanish (B.A.)','Special Divisional Major (B.A. or B.S.)','Statistics (B.A. or B.S.)','Theater Studies (B.A.)',
'Women\'s, Gender, and Sexuality Studies (B.A.)']

#Model for the profile of a student. This info is gathered when the user creates an account
#and is stored in the database so it can be used without getting the user's info every time
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    grad_years = (
        ('2016', '2016'),
        ('2017', '2017'),
        ('2018', '2018'),
        ('2019', '2019'),
    )
    grad_year = models.CharField(max_length=4, choices=grad_years)
    major = models.CharField(max_length=100, choices=[(x,x) for x in majors])
    saved_courses = models.CharField(max_length=800,blank=True,null=True)
    def set_courses(self, x):
        self.saved_courses = json.dumps(x)
        self.saved_courses = [[2,4]]
        print 
    def get_courses(self):
        if self.saved_courses:
            return json.loads(self.saved_courses)
        else:
            return []
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )

#Model to represent all of the user's selections on the search form
class CourseProfile(models.Model):
    course_id = models.IntegerField(blank=True, null=True)
    subject = models.TextField(blank=True, null=True)
    number = models.TextField(blank=True, null=True)
    season = models.IntegerField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    long_title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    skills = (
        ('QR', 'QR (Quantitative Reasoning)'),
        ('L', 'L (Foreign Language)'),
        ('WR', 'WR (Writing)'),
    )
    skill = models.CharField(max_length=2,choices=skills)
    areas = (
        ('SC', 'SC (Sciences)'),
        ('HU','HU (Humanities)'),
        ('SO','SO (Social Sciences)'),
    )
    area = models.CharField(max_length=2,choices=areas)
    average_rating = models.FloatField(blank=True, null=True)
    average_difficulty = models.FloatField(blank=True, null=True)
    num_students = models.IntegerField(blank=True, null=True)
    oci_id = models.IntegerField(blank=True, null=True)
    ybb_id = models.IntegerField(unique=True, blank=True, null=True)

#Model to represent all of the available information about a course
class CompleteData(models.Model):
    id = models.IntegerField(primary_key=True)
    subject = models.TextField(blank=True, null=True)
    num = models.TextField(blank=True, null=True)
    course_id = models.IntegerField(blank=True, null=True)
    season = models.IntegerField(blank=True, null=True)
    shortTitle = models.TextField(blank=True, null=True)
    longTitle = models.TextField(blank=True, null=True)
    average_rating = models.FloatField(blank=True, null=True)
    average_difficulty = models.FloatField(blank=True, null=True)
    num_students = models.IntegerField(blank=True, null=True)
    descrip = models.TextField(db_column='Descrip', blank=True, null=True)  # Field name made lowercase.
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    dist1 = models.TextField(db_column='Dist1', blank=True, null=True)  # Field name made lowercase.
    dist2 = models.TextField(db_column='Dist2', blank=True, null=True)  # Field name made lowercase.
    dist3 = models.TextField(db_column='Dist3', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'complete_data'

#Model to represent how the classes are stored in the YaleAPI
class YaleApiData(models.Model):
    id = models.IntegerField(primary_key=True)
    subject = models.TextField(db_column='Subject', blank=True, null=True)  # Field name made lowercase.
    num = models.TextField(db_column='Num', blank=True, null=True)  # Field name made lowercase.
    shorttitle = models.TextField(db_column='shortTitle', blank=True, null=True)  # Field name made lowercase.
    longtitle = models.TextField(db_column='longTitle', blank=True, null=True)  # Field name made lowercase.
    descrip = models.TextField(db_column='Descrip', blank=True, null=True)  # Field name made lowercase.
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    dist1 = models.TextField(db_column='Dist1', blank=True, null=True)  # Field name made lowercase.
    dist2 = models.TextField(db_column='Dist2', blank=True, null=True)  # Field name made lowercase.
    dist3 = models.TextField(db_column='Dist3', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'yale_API_data'
