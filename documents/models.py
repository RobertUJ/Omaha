from django.db import models
from django.forms.fields import MultipleChoiceField

from projects.models import MainProject


def url(filename):
    ruta = "images/%s/%s" % (str(filename))
    return ruta


class documentsModel(models.Model):
    TYPE_CHOICES = (('1', 'pdf'), ('2', 'docx'),('3', 'image'))
    project = models.ManyToManyField(MainProject)
    name = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=4, choices=TYPE_CHOICES)
    images = models.FileField(null=True, blank=True)
    files = models.FileField(null=True,blank=True)

    def __unicode__(self):
        return "%s" % self.name

