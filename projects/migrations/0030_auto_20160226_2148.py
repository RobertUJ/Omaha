# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0029_auto_20160226_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainproject',
            name='domain',
            field=models.CharField(max_length=100, unique=True, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='mainproject',
            name='name',
            field=models.CharField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='mainproject',
            name='url',
            field=models.CharField(max_length=100, unique=True, null=True, blank=True),
        ),
    ]
