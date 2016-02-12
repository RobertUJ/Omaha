from django.db import models
from projects.models import MainProject


class todolistmodel(models.Model):
    project = models.ManyToManyField(MainProject)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    start_date = models.CharField(max_length=100,null=True, blank=True)
    due_date = models.CharField(max_length=100,null=True, blank=True)
<<<<<<< HEAD
    #user_assigned = models.CharField(max_length=100, null=True, blank=True)
    user_assigner = models.CharField(max_length=100, null=True, blank=True)
=======
>>>>>>> 650d5e1e5550bf772f1817e16505c574f361bae0

    def __unicode__(self):
        return "%s" % self.name
