import datetime
from django.db import models
from projects.models import MainProject


class Module(models.Model):
    project = models.ManyToManyField(MainProject)
    name = models.CharField(unique=True, max_length=50, null=False,default='')
    description = models.TextField(max_length=400, null=True,default='')
    justification = models.TextField(max_length=400, null=True,default='')
    analysis = models.TextField(max_length=400, null=False,default='')
    start_date= models.DateTimeField(unique=True, auto_now_add=True)


    def __unicode__(self):
        return "%s" % self.name