# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_auto_20160202_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainproject',
            name='priority',
            field=models.CharField(default=b'3', max_length=1, null=True, blank=True, choices=[(b'1', b'Para ayer'), (b'2', b'Urgente'), (b'3', b'Para hoy')]),
        ),
    ]
