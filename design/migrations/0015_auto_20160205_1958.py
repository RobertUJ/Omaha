# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0014_auto_20160204_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designmodelrequest',
            name='platform',
            field=models.CharField(max_length=100, choices=[(b'1', b'Ventamovil'), (b'2', b'Tae del sureste'), (b'3', b'Taemarket'), (b'4', b'Movilsa'), (b'5', b'Recarganet'), (b'4', b'DZ productos'), (b'5', b'Maz recargas')]),
        ),
    ]
