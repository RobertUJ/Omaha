# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_remove_mainproject_priority'),
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentsmodel',
            name='project',
            field=models.ManyToManyField(to='projects.MainProject', null=True, blank=True),
        ),
    ]
