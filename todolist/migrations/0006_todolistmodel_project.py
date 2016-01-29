# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_remove_mainproject_tareas'),
        ('todolist', '0005_remove_todolistmodel_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolistmodel',
            name='project',
            field=models.ManyToManyField(to='projects.MainProject'),
        ),
    ]
