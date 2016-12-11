from django.db import models
from django.utils import timezone


class FakeSite(models.Model):
    # Fake site data
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    language = models.CharField(max_length=2, default='en')
    # 
    type = models.IntegerField(default=1)
    
    # Source of fakeness
    source_url = models.CharField(max_length=255)
    source_name = models.CharField(max_length=255)
    source_extra_info = models.CharField(max_length=64)

    comment_from_api = models.CharField(max_length=512)
    

    # When the entry was created
    created = models.DateTimeField(default=timezone.now)
    created_by = models.IntegerField(default=1)

    # Updated when changes made
    updated = models.DateTimeField(default=timezone.now)


