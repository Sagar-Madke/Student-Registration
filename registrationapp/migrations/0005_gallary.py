# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-07 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrationapp', '0004_auto_20161007_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=255)),
                ('upload_image', models.FileField(upload_to='/uploads')),
            ],
        ),
    ]
