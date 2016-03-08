from django.contrib.auth.models import User
from django.db import models

class Entrada(models.Model):
    titulo = models.CharField(max_length=250)
    autor = models.ForeignKey(User, related_name="entradas_blog")
    fecha_pub = models.DateTimeField(auto_now_add=True)
    cuerpo = models.TextField()