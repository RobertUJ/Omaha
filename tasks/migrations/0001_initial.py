# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tasksModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('start_date', models.CharField(max_length=100, null=True, blank=True)),
                ('due_date', models.CharField(max_length=100, null=True, blank=True)),
                ('user_assigned', models.CharField(max_length=100, null=True, blank=True)),
                ('user_assigner', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
    ]
