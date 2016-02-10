# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_remove_mainproject_tareas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainproject',
            name='type',
        ),
    ]
