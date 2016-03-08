# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_remove_mainproject_priority'),
        ('design', '0021_auto_20160216_2324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='designmodelresponse',
            name='project',
        ),
        migrations.AddField(
            model_name='designmodelresponse',
            name='project',
            field=models.ForeignKey(blank=True, to='projects.MainProject', null=True),
        ),
    ]
