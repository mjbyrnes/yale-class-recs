# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yale_class_recs', '0006_completedata_yaleapidata'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='saved_courses',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
