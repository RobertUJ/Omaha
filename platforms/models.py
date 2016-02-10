from django.db import models


class PlatformsModel(models.Model):
    PLATFORMS = (('Ventamovil', 'Ventamovil'),('Tae del sureste', 'Tae del sureste'),('Taemarket', 'Taemarket'),('Movilsa', 'Movilsa'),
                 ('Recarganet', 'Recarganet'),('DZ productos', 'DZ productos'), ('Maz recargas', 'Maz recargas'),)

    def __unicode__(self):
        return "%s" % self.name


class TypesModel(models.Model):
    TYPES = (('Android', 'Android'),('Host', 'Host'), ('Java', 'Java'),('Web', 'Web'),
                 ('SMS', 'Sms'),('Windows app', 'Windows app'),('Whatsapp', 'Whatsapp'),)

    def __unicode__(self):
        return "%s" % self.name

