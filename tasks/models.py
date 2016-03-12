from django.contrib.auth.models import User
from django.db import models
from projects.models import MainProject
from todolist.models import todolistmodel


class tasksModel(models.Model):
    project = models.ManyToManyField(MainProject)
    todolist = models.ManyToManyField(todolistmodel)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    start_date = models.DateField(auto_now_add=True,null=True)
    due_date = models.DateField(null=True)
    user_assigned = models.CharField(max_length=50,null=True,blank=True)
    user_assigner = models.CharField(max_length=50,null=True)

    def __unicode__(self):
        return "%s" % self.name
