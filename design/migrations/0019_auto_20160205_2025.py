# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0018_auto_20160205_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='designmodelrequest',
            name='platform',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'Ventamovil', b'Ventamovil'), (b'Tae del sureste', b'Tae del sureste'), (b'Taemarket', b'Taemarket'), (b'Movilsa', b'Movilsa'), (b'Recarganet', b'Recarganet'), (b'DZ productos', b'DZ productos'), (b'Maz recargas', b'Maz recargas')]),
        ),
        migrations.AddField(
            model_name='designmodelrequest',
            name='type',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'Android', b'Android'), (b'Host', b'Host'), (b'Java', b'Java'), (b'Web', b'Web'), (b'SMS', b'Sms'), (b'Windows app', b'Windows app'), (b'Whatsapp', b'Whatsapp')]),
        ),
        migrations.AddField(
            model_name='designmodelresponse',
            name='platform',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'Ventamovil', b'Ventamovil'), (b'Tae del sureste', b'Tae del sureste'), (b'Taemarket', b'Taemarket'), (b'Movilsa', b'Movilsa'), (b'Recarganet', b'Recarganet'), (b'DZ productos', b'DZ productos'), (b'Maz recargas', b'Maz recargas')]),
        ),
        migrations.AddField(
            model_name='designmodelresponse',
            name='type',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'Android', b'Android'), (b'Host', b'Host'), (b'Java', b'Java'), (b'Web', b'Web'), (b'SMS', b'Sms'), (b'Windows app', b'Windows app'), (b'Whatsapp', b'Whatsapp')]),
        ),
    ]
