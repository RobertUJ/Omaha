from django.db import models
from projects.models import MainProject


class ticketsModel(models.Model):
    PRIORITY = (('1', 'Para ayer'),('2', 'Urgente'),('3', 'Para hoy'),)
    project = models.ManyToManyField(MainProject)
    description = models.CharField(max_length=200)
    user_reporter = models.CharField(max_length=100, blank=True, null=True)
    user_assigned = models.CharField(max_length=100)
    priority = models.CharField(max_length=1, choices=PRIORITY)

    def __unicode__(self):
        return "%s" % self.description
