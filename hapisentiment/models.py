from django.db import models

# Create your models here.
from django.utils import timezone


class SentimentData(models.Model):
    words = models.CharField(max_length=2048)
    url = models.CharField(max_length=255)
    containsHateSpeech = models.BooleanField()
    score = models.IntegerField(default=0)
    created =  models.DateTimeField(default=timezone.now)