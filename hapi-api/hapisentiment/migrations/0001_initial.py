# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-29 15:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SentimentData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('words', models.CharField(max_length=2048)),
                ('url', models.CharField(max_length=255)),
                ('containsHateSpeech', models.BooleanField()),
                ('score', models.IntegerField(default=0)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
