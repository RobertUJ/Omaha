# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20160128_2027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainproject',
            name='tareas',
        ),
    ]
