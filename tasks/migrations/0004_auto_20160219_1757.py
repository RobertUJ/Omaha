# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0010_auto_20160218_2321'),
        ('projects', '0019_remove_mainproject_priority'),
        ('tasks', '0003_tasksmodel_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasksmodel',
            name='project',
        ),
        migrations.AddField(
            model_name='tasksmodel',
            name='project',
            field=models.ForeignKey(blank=True, to='projects.MainProject', null=True),
        ),
        migrations.RemoveField(
            model_name='tasksmodel',
            name='todolist',
        ),
        migrations.AddField(
            model_name='tasksmodel',
            name='todolist',
            field=models.ForeignKey(blank=True, to='todolist.todolistmodel', null=True),
        ),
    ]
