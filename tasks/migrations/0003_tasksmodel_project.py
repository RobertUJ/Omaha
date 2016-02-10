# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_auto_20160202_2054'),
        ('tasks', '0002_tasksmodel_todolist'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasksmodel',
            name='project',
            field=models.ManyToManyField(to='projects.MainProject'),
        ),
    ]
