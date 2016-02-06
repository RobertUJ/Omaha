from django.db import models

# Create your models here.

# Create your models here.
class Module(models.Model):
    name = models.CharField(max_length=50,null=False,default='')
    description = models.TextField(max_length=200,null=True,default='')
    justification = models.TextField(max_length=200,null=True,default='')
    analysis = models.TextField(max_length=200,null=False,default='')
    start_date= start_date = models.DateTimeField()


    def __unicode__(self):
        return "%s" % self.name