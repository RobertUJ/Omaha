# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_auto_20160122_0712'),
        ('projects', '0006_auto_20160122_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainproject',
            name='todolistmodel',
            field=models.ManyToManyField(to='todolist.todolistmodel'),
        ),
    ]
