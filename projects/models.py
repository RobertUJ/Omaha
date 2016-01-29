from django.db import models

class MainProject(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    url = models.CharField(max_length=100, null=True, blank=True)
    domain = models.CharField(max_length=100, null=True, blank=True)
    server_assigned = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    client = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    priority = models.IntegerField()
    users = models.CharField(max_length=100, null=True, blank=True)
    # tareas	= models.ManyToManyField(todolistmodel,null=True,blank=True)
    def __unicode__(self):
        return "%s" % self.name


