# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-06 07:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hapifakenews', '0003_auto_20161206_0731'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fakesite',
            old_name='createdby',
            new_name='created_by',
        ),
    ]