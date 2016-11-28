# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FakeNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('source', models.CharField(max_length=255)),
                ('isFake', models.BooleanField()),
            ],
        ),
    ]
