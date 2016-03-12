# -*- encoding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models


class DiscussionModel(models.Model):
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
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default="projects")

    def __unicode__(self):
        return "%s" % self.category

class CommentModel(models.Model):
    title = models.CharField(max_length=250)
    date_pub = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, null=True, blank=True)
    body = models.TextField()
    discussion = models.ForeignKey(DiscussionModel)

    def __unicode__(self):
        return "%s" % self.title
