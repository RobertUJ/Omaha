from django.contrib.auth.models import User
from django.db import models
from django.http import request

from platforms.models import PlatformsModel


class MainProject(models.Model):
    PRIORITY = (('1', 'Para ayer'),('2', 'Urgente'),('3', 'Para hoy'),)
    user = models.ForeignKey(User, null=True, blank=True)
    name = models.CharField(unique=True, max_length=100)
    start_date = models.DateField(null=False, auto_now_add=True)
    due_date = models.DateField(null=False, blank=True)
    url = models.CharField(unique=True, max_length=100, null=True, blank=True)
    domain = models.CharField(max_length=100, null=True, blank=True)
    server = models.CharField(max_length=100, null=True, blank=True)
    client = models.CharField(max_length=100)
    platform = models.CharField(max_length=100, choices=PlatformsModel.PLATFORMS)
    users = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return "%s" % self.name

