from django.db import models
from projects.models import MainProject


def url(filename):
    ruta = "images/%s/%s" % (str(filename))
    return ruta


class ticketsModel(models.Model):
    PRIORITY = (('1', 'Para ayer'),('2', 'Urgente'),('3', 'Para hoy'),)
    STATUS = (('1', 'Pendiente'),('2', 'Resuelto'),)
    project = models.ManyToManyField(MainProject)
    description = models.CharField(max_length=200)
    files = models.FileField(null=True, blank=True)
    user_reporter = models.CharField(max_length=100, blank=True, null=True)
    user_assigned = models.CharField(max_length=100)
    priority = models.CharField(max_length=1, choices=PRIORITY)
    status = models.CharField(max_length=1, choices=STATUS, default='1', blank=True, null=True)

    def __unicode__(self):
        return "%s" % self.description

class ticketsModelResponse(models.Model):
    STATUS = (('1', 'Pendiente'),('2', 'Resuelto'),)
    response = models.CharField(max_length=200)
    files = models.FileField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS, default='1', blank=True, null=True)
    ticket_status = models.ForeignKey(ticketsModel,default='1')

    def __unicode__(self):
        return "%s" % self.response