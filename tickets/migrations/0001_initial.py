# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_auto_20160202_2054'),
    ]

    operations = [
        migrations.CreateModel(
            name='ticketsModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=200)),
                ('user_reporter', models.CharField(max_length=100, null=True, blank=True)),
                ('user_assigned', models.CharField(max_length=100)),
                ('priority', models.CharField(max_length=1, choices=[(b'1', b'Para ayer'), (b'2', b'Urgente'), (b'3', b'Para hoy')])),
                ('project', models.ManyToManyField(to='projects.MainProject')),
            ],
        ),
    ]
