# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-08 04:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrationapp', '0006_auto_20161007_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallary',
            name='description',
            field=models.TextField(),
        ),
    ]