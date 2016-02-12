from django.db import models
from platforms.models import PlatformsModel


class MainProject(models.Model):
    priority_choice = (('1', 'Para ayer'),('2', 'Urgente'),('3', 'Para hoy'),)
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    due_date = models.DateField()
    url = models.CharField(max_length=100, null=True, blank=True)
    domain = models.CharField(max_length=100, null=True, blank=True)
    server = models.CharField(max_length=100, null=True, blank=True)
    client = models.CharField(max_length=100)
<<<<<<< HEAD
    platform = models.CharField(max_length=100)
    priority = models.CharField(max_length=1, choices=priority_choice,default='3',null=True,blank=True)
=======
    platform = models.CharField(max_length=100, choices=PlatformsModel.PLATFORMS)
>>>>>>> 650d5e1e5550bf772f1817e16505c574f361bae0
    users = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return "%s" % self.name

