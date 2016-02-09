# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
# Create your models here.


class UserProfile(models.Model):
    #user = models.OneToOneField(User, unique=True, related_name='Perfil')
    user = models.ForeignKey(User, unique=True, related_name='perfil')
    #photo = models.ImageField(upload_to='UserProfile',blank=True,null=True)
    descripcion = models.TextField(max_length=200, default='',blank=True)
    def __unicode__(self):
        return "%s" % self.user


