# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DesignModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_assigner', models.CharField(max_length=100)),
                ('assignment', models.CharField(max_length=100)),
                ('files', models.ImageField(upload_to=b'')),
                ('platform', models.CharField(max_length=100, null=True, blank=True)),
                ('type', models.CharField(max_length=100, null=True, blank=True)),
                ('asked_date', models.CharField(max_length=100, null=True, blank=True)),
                ('resolved_date', models.CharField(max_length=100, null=True, blank=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
