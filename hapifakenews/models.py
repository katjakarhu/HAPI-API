from django.db import models
from django.utils import timezone


class FakeSite(models.Model):
    # Fake site data
    site = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    # Fake news = 1, etc
    type = models.IntegerField(default=1)


    # Source of fakeness
    sourceurl = models.CharField(max_length=255, default='')
    sourcename = models.CharField(max_length=255, default = '')

    # When the entry was created
    created = models.DateTimeField(default=timezone.now)
    createdby = models.IntegerField(default=1)

    # Updated when changes made
    updated = models.DateTimeField(default=timezone.now)


