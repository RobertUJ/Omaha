import datetime
from django.db import models

# Create your models here.

# Create your models here.
class Module(models.Model):
    name = models.CharField(max_length=50, null=False,default='')
    description = models.TextField(max_length=400, null=True,default='')
    justification = models.TextField(max_length=400, null=True,default='')
    analysis = models.TextField(max_length=400, null=False,default='')
    start_date= models.DateTimeField(auto_now_add=True)


    def __unicode__(self):
        return "%s" % self.name