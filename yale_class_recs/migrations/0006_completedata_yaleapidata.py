# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yale_class_recs', '0005_auto_20151217_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompleteData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.TextField(null=True, blank=True)),
                ('number', models.TextField(null=True, blank=True)),
                ('ybb_id', models.IntegerField(null=True, blank=True)),
                ('season', models.IntegerField(null=True, blank=True)),
                ('title', models.TextField(null=True, blank=True)),
                ('long_title', models.TextField(null=True, blank=True)),
                ('average_rating', models.FloatField(null=True, blank=True)),
                ('average_difficulty', models.FloatField(null=True, blank=True)),
                ('num_students', models.IntegerField(null=True, blank=True)),
                ('descrip', models.TextField(null=True, db_column='Descrip', blank=True)),
                ('time', models.TextField(null=True, db_column='Time', blank=True)),
                ('dist1', models.TextField(null=True, db_column='Dist1', blank=True)),
                ('dist2', models.TextField(null=True, db_column='Dist2', blank=True)),
                ('dist3', models.TextField(null=True, db_column='Dist3', blank=True)),
            ],
            options={
                'db_table': 'complete_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='YaleApiData',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('subject', models.TextField(null=True, db_column='Subject', blank=True)),
                ('num', models.TextField(null=True, db_column='Num', blank=True)),
                ('shorttitle', models.TextField(null=True, db_column='shortTitle', blank=True)),
                ('longtitle', models.TextField(null=True, db_column='longTitle', blank=True)),
                ('descrip', models.TextField(null=True, db_column='Descrip', blank=True)),
                ('time', models.TextField(null=True, db_column='Time', blank=True)),
                ('dist1', models.TextField(null=True, db_column='Dist1', blank=True)),
                ('dist2', models.TextField(null=True, db_column='Dist2', blank=True)),
                ('dist3', models.TextField(null=True, db_column='Dist3', blank=True)),
            ],
            options={
                'db_table': 'yale_API_data',
                'managed': False,
            },
        ),
    ]
