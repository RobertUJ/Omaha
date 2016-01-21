# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20160119_0302'),
    ]

    operations = [
        migrations.CreateModel(
            name='addProject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('start_date', models.CharField(max_length=100)),
                ('end_date', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100, null=True, blank=True)),
                ('domain', models.CharField(max_length=100, null=True, blank=True)),
                ('server_assigned', models.CharField(max_length=100, null=True, blank=True)),
                ('type', models.CharField(max_length=100, null=True, blank=True)),
                ('client', models.CharField(max_length=100)),
                ('platform', models.CharField(max_length=100)),
                ('priority', models.CharField(max_length=100)),
                ('users', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
            },
        ),
    ]
