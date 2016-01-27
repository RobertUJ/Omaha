# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DesignModelRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_assigner', models.CharField(max_length=100)),
                ('assignment', models.CharField(max_length=100)),
                ('platform', models.CharField(max_length=100, null=True, blank=True)),
                ('type', models.CharField(max_length=100, null=True, blank=True)),
                ('asked_date', models.CharField(max_length=100, null=True, blank=True)),
                ('tentative_date', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DesignModelResponse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('designer_assigned', models.CharField(max_length=100)),
                ('user_assigner', models.CharField(max_length=100)),
                ('assignment', models.CharField(max_length=100)),
                ('files', models.ImageField(upload_to=b'')),
                ('platform', models.CharField(max_length=100, null=True, blank=True)),
                ('type', models.CharField(max_length=100, null=True, blank=True)),
                ('coment', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='DesignModel',
        ),
    ]
