# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-07 08:27
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('registrationapp', '0002_auto_20161007_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='dob',
            field=models.DateField(),
        ),
    ]
