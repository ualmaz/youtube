from django.db import models
import datetime
from django.urls import reverse
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import User

class Video(models.Model):
    link = models.URLField()

    def __unicode__(self):
        return self.link

class Calendar(models.Model):
    title = models.CharField('Event title:', max_length=100)
    content = models.CharField('Content:', max_length=100, default='')
    date_posted = models.DateField(default=timezone.now)
    date_from = models.DateField()
    date_to = models.DateField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    link = models.CharField('Link:', max_length=250, blank=True, null=True)


    def __str__(self):
        return '%s' % self.title
