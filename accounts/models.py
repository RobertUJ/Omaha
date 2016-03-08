from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='perfil', unique=True)
    photo = models.FileField(blank=True, null=True)
    def __unicode__(self):
        return "%s" % self.user

