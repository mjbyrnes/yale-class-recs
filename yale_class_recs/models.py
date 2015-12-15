# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

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
        ('QR', 'QR'),
        ('L', 'L'),
        ('WR', 'WR'),
    )
    skill = models.CharField(max_length=2,choices=skills)
    areas = (
        ('SC', 'SC'),
        ('HU','HU'),
        ('SO','SO'),
    )
    area = models.CharField(max_length=2,choices=areas)
    average_rating = models.FloatField(blank=True, null=True)
    average_difficulty = models.FloatField(blank=True, null=True)
    num_students = models.IntegerField(blank=True, null=True)
    oci_id = models.IntegerField(blank=True, null=True)
    ybb_id = models.IntegerField(unique=True, blank=True, null=True)

class EvaluationComments(models.Model):
    id = models.IntegerField(primary_key=True, blank=True, null=False)  # AutoField?
    course_id = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    comment_length = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evaluation_comments'
        unique_together = (('course_id', 'type', 'comment'),)


class EvaluationCourseNames(models.Model):
    id = models.IntegerField(primary_key=True, blank=True, null=False)  # AutoField?
    course_id = models.IntegerField(blank=True, null=True)
    subject = models.TextField(blank=True, null=True)
    number = models.TextField(blank=True, null=True)
    section = models.IntegerField(blank=True, null=True)
    season = models.IntegerField(blank=True, null=True)
    oci_id = models.IntegerField(blank=True, null=True)
    ybb_id = models.IntegerField(unique=True, blank=True, null=True)
    rating_1 = models.IntegerField(blank=True, null=True)
    rating_2 = models.IntegerField(blank=True, null=True)
    rating_3 = models.IntegerField(blank=True, null=True)
    rating_4 = models.IntegerField(blank=True, null=True)
    rating_5 = models.IntegerField(blank=True, null=True)
    difficulty_1 = models.IntegerField(blank=True, null=True)
    difficulty_2 = models.IntegerField(blank=True, null=True)
    difficulty_3 = models.IntegerField(blank=True, null=True)
    difficulty_4 = models.IntegerField(blank=True, null=True)
    difficulty_5 = models.IntegerField(blank=True, null=True)
    major_0 = models.IntegerField(blank=True, null=True)
    major_1 = models.IntegerField(blank=True, null=True)
    requirements_0 = models.IntegerField(blank=True, null=True)
    requirements_1 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evaluation_course_names'
        unique_together = (('subject', 'number', 'section', 'season'),)


class EvaluationCourses(models.Model):
    id = models.IntegerField(primary_key=True, blank=True, null=False)  # AutoField?
    season = models.IntegerField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    long_title = models.TextField(blank=True, null=True)
    average_rating = models.FloatField(blank=True, null=True)
    average_difficulty = models.FloatField(blank=True, null=True)
    num_students = models.IntegerField(blank=True, null=True)
    rating_1 = models.IntegerField(blank=True, null=True)
    rating_2 = models.IntegerField(blank=True, null=True)
    rating_3 = models.IntegerField(blank=True, null=True)
    rating_4 = models.IntegerField(blank=True, null=True)
    rating_5 = models.IntegerField(blank=True, null=True)
    difficulty_1 = models.IntegerField(blank=True, null=True)
    difficulty_2 = models.IntegerField(blank=True, null=True)
    difficulty_3 = models.IntegerField(blank=True, null=True)
    difficulty_4 = models.IntegerField(blank=True, null=True)
    difficulty_5 = models.IntegerField(blank=True, null=True)
    major_0 = models.IntegerField(blank=True, null=True)
    major_1 = models.IntegerField(blank=True, null=True)
    requirements_0 = models.IntegerField(blank=True, null=True)
    requirements_1 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evaluation_courses'


class EvaluationProfessors(models.Model):
    id = models.IntegerField(primary_key=True, blank=True, null=False)  # AutoField?
    course_id = models.IntegerField(blank=True, null=True)
    professor = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evaluation_professors'
        unique_together = (('professor', 'course_id'),)
