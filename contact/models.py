from django.db import models


class ContactModel(models.Model):
    name = models.CharField(max_length=200,null=False,blank=False)
    email = models.EmailField(max_length=200,null=False,blank=False)
    comment = models.TextField(max_length=200,null=False,blank=False)

    def __unicode__(self):
        return "%s" % self.nombre_completo

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'


class CuentasAdmin(models.Model):
    nombre = models.CharField(max_length=200,null=False,blank=False)
    correo = models.EmailField(max_length=200,null=False,blank=False)
    activo = models.BooleanField()

    def __unicode__(self):
        return "%s" % self.nombre
