# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_documentsmodel_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentsmodel',
            name='project',
            field=models.ManyToManyField(to='projects.MainProject'),
        ),
    ]
