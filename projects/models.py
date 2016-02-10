from django.db import models
# from todolist.models import todolistmodel


class MainProject(models.Model):
    PRIORITY = (('1', 'Para ayer'),('2', 'Urgente'),('3', 'Para hoy'),)
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    due_date = models.DateField()
    url = models.CharField(max_length=100, null=True, blank=True)
    domain = models.CharField(max_length=100, null=True, blank=True)
    server = models.CharField(max_length=100, null=True, blank=True)
    client = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    priority = models.CharField(max_length=1, choices=PRIORITY)
    users = models.CharField(max_length=100, null=True, blank=True)
    def __unicode__(self):
        return "%s" % self.name


