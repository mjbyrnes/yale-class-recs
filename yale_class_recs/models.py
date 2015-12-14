# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


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
