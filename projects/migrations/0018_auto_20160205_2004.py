# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0017_auto_20160205_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainproject',
            name='platform',
            field=models.CharField(max_length=100, choices=[(b'Ventamovil', b'Ventamovil'), (b'Tae del sureste', b'Tae del sureste'), (b'Taemarket', b'Taemarket'), (b'Movilsa', b'Movilsa'), (b'Recarganet', b'Recarganet'), (b'DZ productos', b'DZ productos'), (b'Maz recargas', b'Maz recargas')]),
        ),
    ]
