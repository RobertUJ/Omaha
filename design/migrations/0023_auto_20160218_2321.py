# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_remove_mainproject_priority'),
        ('design', '0022_auto_20160218_2312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='designmodelrequest',
            name='project',
        ),
        migrations.AddField(
            model_name='designmodelrequest',
            name='project',
            field=models.ForeignKey(blank=True, to='projects.MainProject', null=True),
        ),
    ]
