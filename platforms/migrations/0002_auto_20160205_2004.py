# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platforms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platformsmodel',
            name='priority',
            field=models.CharField(max_length=1, choices=[(b'Ventamovil', b'Ventamovil'), (b'Tae del sureste', b'Tae del sureste'), (b'Taemarket', b'Taemarket'), (b'Movilsa', b'Movilsa'), (b'Recarganet', b'Recarganet'), (b'DZ productos', b'DZ productos'), (b'Maz recargas', b'Maz recargas')]),
        ),
    ]
