
from django.db import models

from platforms.models import PlatformsModel, TypesModel
from projects.models import MainProject


def url(filename):
    ruta = "images/%s/%s" % (str(filename))
    return ruta


class DesignModelRequest(models.Model):
    project = models.ManyToManyField(MainProject)
    user_assigner = models.CharField(max_length=100, null=True, blank=True)
    assignment = models.CharField(max_length=100)
    platform = models.CharField(max_length=100, choices=PlatformsModel.PLATFORMS, blank=True, null=True)
    type = models.CharField(max_length=100, choices=TypesModel.TYPES, blank=True, null=True)
    asked_date = models.DateField(max_length=100, null=True, blank=True)
    tentative_date = models.DateField(max_length=100, null=True, blank=True)
    comment = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return "%s" % self.assignment


class DesignModelResponse(models.Model):
    project = models.ManyToManyField(MainProject)
    designer_assigned = models.CharField(max_length=100)
    user_assigner = models.CharField(max_length=100, null=True, blank=True)
    assignment = models.CharField(max_length=100, null=True, blank=True)
    files = models.FileField(null=True,blank=True)
    platform = models.CharField(max_length=100, choices=PlatformsModel.PLATFORMS, blank=True, null=True)
    type = models.CharField(max_length=100, choices=TypesModel.TYPES, blank=True, null=True)
    comment = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return "%s" % self.assignment

from django.db import models


class DesignMailModel(models.Model):
    subject = models.CharField(max_length=200,null=False,blank=False)
    email = models.EmailField(max_length=200,null=False,blank=False)

    def __unicode__(self):
        return "%s" % self.nombre_completo

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'
