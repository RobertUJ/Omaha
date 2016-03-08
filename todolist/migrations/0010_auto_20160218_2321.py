# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_remove_mainproject_priority'),
        ('todolist', '0009_auto_20160208_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolistmodel',
            name='project',
        ),
        migrations.AddField(
            model_name='todolistmodel',
            name='project',
            field=models.ForeignKey(blank=True, to='projects.MainProject', null=True),
        ),
    ]
