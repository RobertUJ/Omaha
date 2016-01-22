<<<<<<< HEAD
from django.db import models

def url(filename):
    ruta = "images/%s/%s" % (str(filename))
    return ruta

class DesignModelRequest(models.Model):
    user_assigner = models.CharField(max_length=100)
    assignment = models.CharField(max_length=100)
    platform = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    asked_date = models.DateTimeField(max_length=100, null=True, blank=True)
    tentative_date = models.DateTimeField(max_length=100, null=True, blank=True)
    comment = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return "%s" % self.assignment


class DesignModelResponse(models.Model):


    designer_assigned = models.CharField(max_length=100)
    user_assigner = models.CharField(max_length=100)
    assignment = models.CharField(max_length=100)
    files = models.ImageField(upload_to=url,null=True,blank=True)
    platform = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    coment = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return "%s" % self.assignment
=======
from __future__ import unicode_literals

from django.db import models

# Create your models here.
>>>>>>> 84bb6d606d47a31bfc3d0127ab829f743e58f464
