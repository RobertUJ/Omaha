# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_auto_20160205_1930'),
        ('todolist', '0007_remove_todolistmodel_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolistmodel',
            name='project',
            field=models.ManyToManyField(to='projects.MainProject'),
        ),
    ]
