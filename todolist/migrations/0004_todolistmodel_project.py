# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 20:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_auto_20160128_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolistmodel',
            name='project',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
