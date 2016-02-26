# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0027_remove_mainproject_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainproject',
            name='name',
            field=models.CharField(unique=True, max_length=100, blank=True),
        ),
    ]
