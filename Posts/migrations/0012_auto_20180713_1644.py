# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-13 11:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0011_auto_20180704_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2018, 7, 13, 11, 14, 42, 986572, tzinfo=utc)),
        ),
    ]
