# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-22 07:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolistmodel',
            old_name='server_assigner',
            new_name='user_assigner',
        ),
    ]
