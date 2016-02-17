from django.db import models
from platforms.models import PlatformsModel


class MainProject(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    due_date = models.DateField()
    url = models.CharField(max_length=100, null=True, blank=True)
    domain = models.CharField(max_length=100, null=True, blank=True)
    server = models.CharField(max_length=100, null=True, blank=True)
    client = models.CharField(max_length=100)
    platform = models.CharField(max_length=100, choices=PlatformsModel.PLATFORMS)
    users = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return "%s" % self.name

