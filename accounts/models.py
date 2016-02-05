# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
# Create your models here.


class UserProfile(models.Model):
    #user = models.OneToOneField(User, unique=True, related_name='Perfil')
    user = models.ForeignKey(User, unique=True, related_name='perfil')

    comentario = models.TextField(max_length=100, default='')
    photo = models.ImageField(upload_to='UserProfile',blank=True,null=True)

    #def __str__(self):
     #   return self.UserProfile.user


