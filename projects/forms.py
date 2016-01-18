from django.db import models


class MainProject(models.Model):
    project_name = models.CharField(max_length=100)
    project_start_date = models.DateTimeField()
    project_end_date = models.DateTimeField()
    project_url = models.CharField(max_length=100, null=True, blank=True)
    project_domain = models.CharField(max_length=100, null=True, blank=True)
    project_server_assigned = models.CharField(max_length=100, null=True, blank=True)
    project_type = models.CharField(max_length=100, null=True, blank=True)
    project_client = models.CharField(max_length=100)
    project_platform = models.CharField(max_length=100)
    project_priority = models.IntegerField()
    project_users = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return "%s" % self.project_name