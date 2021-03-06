# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-13 23:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EvaluationComments',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('course_id', models.IntegerField(blank=True, null=True)),
                ('type', models.IntegerField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('comment_length', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'evaluation_comments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EvaluationCourseNames',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('course_id', models.IntegerField(blank=True, null=True)),
                ('subject', models.TextField(blank=True, null=True)),
                ('number', models.TextField(blank=True, null=True)),
                ('section', models.IntegerField(blank=True, null=True)),
                ('season', models.IntegerField(blank=True, null=True)),
                ('oci_id', models.IntegerField(blank=True, null=True)),
                ('ybb_id', models.IntegerField(blank=True, null=True, unique=True)),
                ('rating_1', models.IntegerField(blank=True, null=True)),
                ('rating_2', models.IntegerField(blank=True, null=True)),
                ('rating_3', models.IntegerField(blank=True, null=True)),
                ('rating_4', models.IntegerField(blank=True, null=True)),
                ('rating_5', models.IntegerField(blank=True, null=True)),
                ('difficulty_1', models.IntegerField(blank=True, null=True)),
                ('difficulty_2', models.IntegerField(blank=True, null=True)),
                ('difficulty_3', models.IntegerField(blank=True, null=True)),
                ('difficulty_4', models.IntegerField(blank=True, null=True)),
                ('difficulty_5', models.IntegerField(blank=True, null=True)),
                ('major_0', models.IntegerField(blank=True, null=True)),
                ('major_1', models.IntegerField(blank=True, null=True)),
                ('requirements_0', models.IntegerField(blank=True, null=True)),
                ('requirements_1', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'evaluation_course_names',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EvaluationCourses',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('season', models.IntegerField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('long_title', models.TextField(blank=True, null=True)),
                ('average_rating', models.FloatField(blank=True, null=True)),
                ('average_difficulty', models.FloatField(blank=True, null=True)),
                ('num_students', models.IntegerField(blank=True, null=True)),
                ('rating_1', models.IntegerField(blank=True, null=True)),
                ('rating_2', models.IntegerField(blank=True, null=True)),
                ('rating_3', models.IntegerField(blank=True, null=True)),
                ('rating_4', models.IntegerField(blank=True, null=True)),
                ('rating_5', models.IntegerField(blank=True, null=True)),
                ('difficulty_1', models.IntegerField(blank=True, null=True)),
                ('difficulty_2', models.IntegerField(blank=True, null=True)),
                ('difficulty_3', models.IntegerField(blank=True, null=True)),
                ('difficulty_4', models.IntegerField(blank=True, null=True)),
                ('difficulty_5', models.IntegerField(blank=True, null=True)),
                ('major_0', models.IntegerField(blank=True, null=True)),
                ('major_1', models.IntegerField(blank=True, null=True)),
                ('requirements_0', models.IntegerField(blank=True, null=True)),
                ('requirements_1', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'evaluation_courses',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EvaluationProfessors',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('course_id', models.IntegerField(blank=True, null=True)),
                ('professor', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'evaluation_professors',
                'managed': False,
            },
        ),
    ]
