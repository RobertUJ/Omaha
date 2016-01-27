# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
from django.conf import settings


class UserProfile(models.Model):
    username = models.CharField(max_length=100, blank=False, null=False,default="")
    email = models.EmailField(max_length=100, default='user@email.com')
    password = models.CharField(max_length=50,blank=False,null=False,default="")

   # photo = models.ImageField(upload_to='profiles',blank=True,null=True)

    #def __str__(self):
        #return self.UserProfile.username


