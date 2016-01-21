from django.db import models

# Create your models here.
class MainUsers(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s" % self.name