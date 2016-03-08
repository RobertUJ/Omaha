# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_ticketsmodel_files'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketsmodel',
            name='status',
            field=models.CharField(default=b'1', max_length=1, null=True, blank=True, choices=[(b'1', b'Pendiente'), (b'2', b'Resuelto')]),
        ),
    ]
