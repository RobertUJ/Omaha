from django.db import models

class todolistmodel(models.Model):
    name = models.CharField(max_length=100)
    task = models.CharField(max_length=100)
    start_date = models.CharField(max_length=100,null=True, blank=True)
    end_date = models.CharField(max_length=100,null=True, blank=True)
    user_assigned = models.CharField(max_length=100, null=True, blank=True)
    user_assigner = models.CharField(max_length=100, null=True, blank=True)
    platform = models.CharField(max_length=100)
    priority = models.IntegerField()

    def __unicode__(self):
        return "%s" % self.name