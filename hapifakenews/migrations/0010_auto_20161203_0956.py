# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-03 09:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hapifakenews', '0009_auto_20161203_0934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fakesite',
            name='ratingfromsource',
        ),
        migrations.AddField(
            model_name='fakesite',
            name='ratingatsource',
            field=models.CharField(default='', max_length=64),
        ),
    ]
