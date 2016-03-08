# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_ticketsmodel_files'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticketsmodel',
            name='files',
        ),
    ]
