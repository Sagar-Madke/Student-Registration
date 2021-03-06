# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-07 08:09
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('registrationapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='id',
        ),
        migrations.AddField(
            model_name='register',
            name='dob',
            field=models.DateTimeField(default=timezone.now),
        ),
        migrations.AlterField(
            model_name='register',
            name='reg_no',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='register',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
