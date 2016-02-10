# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
# Create your models here.


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True, related_name='perfil')
    descripcion = models.TextField(max_length=200, default='',blank=True)
    photo = models.FileField(blank=True, null=True)
    def __unicode__(self):
        return "%s" % self.user


