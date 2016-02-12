# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlatformsModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('priority', models.CharField(max_length=1, choices=[(b'1', b'Ventamovil'), (b'2', b'Tae del sureste'), (b'3', b'Taemarket'), (b'4', b'Movilsa'), (b'5', b'Recarganet'), (b'4', b'DZ productos'), (b'5', b'Maz recargas')])),
            ],
        ),
    ]
