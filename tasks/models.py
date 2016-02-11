from django.db import models
from projects.models import MainProject
from todolist.models import todolistmodel


class tasksModel(models.Model):
    project = models.ManyToManyField(MainProject)
    todolist = models.ManyToManyField(todolistmodel)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    start_date = models.CharField(max_length=100,null=True, blank=True)
    due_date = models.CharField(max_length=100,null=True, blank=True)
    user_assigned = models.CharField(max_length=100, null=True, blank=True)
    user_assigner = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return "%s" % self.name
