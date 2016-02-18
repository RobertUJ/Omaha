# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_remove_mainproject_priority'),
        ('modules', '0008_auto_20160209_0500'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='project',
            field=models.ManyToManyField(to='projects.MainProject'),
        ),
    ]
