# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-03 19:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0008_auto_20180704_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2018, 7, 3, 19, 24, 44, 711856, tzinfo=utc)),
        ),
    ]