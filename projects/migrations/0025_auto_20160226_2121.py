# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0024_auto_20160226_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainproject',
            name='domain',
            field=models.CharField(max_length=100, unique=True, null=True, blank=True),
        ),
    ]
