# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20160129_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainproject',
            name='priority',
            field=models.CharField(max_length=1, choices=[(b'1', b'Para ayer'), (b'2', b'Urgente'), (b'3', b'Para hoy')]),
        ),
    ]
