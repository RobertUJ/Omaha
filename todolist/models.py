from django.db import models
from projects.models import MainProject


class todolistmodel(models.Model):
    project = models.ManyToManyField(MainProject)
    name = models.CharField(unique=True, max_length=100)
    description = models.CharField(max_length=100)
    start_date = models.DateField(auto_now_add=True, null=False, blank=False)
    due_date = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return "%s" % self.name
