# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0028_mainproject_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainproject',
            name='domain',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='mainproject',
            name='name',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='mainproject',
            name='url',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
