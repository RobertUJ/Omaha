# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0006_todolistmodel_project'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasksmodel',
            name='todolist',
            field=models.ManyToManyField(to='todolist.todolistmodel'),
        ),
    ]
