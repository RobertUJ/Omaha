# -*- encoding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models


class Discussion(models.Model):
    id_category = models.IntegerField(null=True)
    CATEGORY_CHOICES = (
        ('projects','Proyectos'),
        ('modules','Modulos'),
        ('todos','Listas'),
        ('tasks','Tareas'),
        ('design','Diseño'),
        ('docs','Documentos'),
        ('tickesys','Tickets'),
    )
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, null=True)

    def __unicode__(self):
        return "%s" % self.category

class Comment(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, related_name="entradas_blog")
    date_pub = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    Discussion = models.ManyToManyField(Discussion)

    def __unicode__(self):
        return "%s" % self.title
