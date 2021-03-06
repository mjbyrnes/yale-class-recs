# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-17 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yale_class_recs', '0003_auto_20151217_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseprofile',
            name='average_difficulty',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
        migrations.AlterField(
            model_name='courseprofile',
            name='average_rating',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=5),
            preserve_default=False,
        ),
    ]
