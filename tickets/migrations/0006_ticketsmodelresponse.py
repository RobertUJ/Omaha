# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0005_ticketsmodel_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ticketsModelResponse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('response', models.CharField(max_length=200)),
                ('files', models.FileField(null=True, upload_to=b'', blank=True)),
                ('status', models.CharField(default=b'1', max_length=1, null=True, blank=True, choices=[(b'1', b'Pendiente'), (b'2', b'Resuelto')])),
            ],
        ),
    ]
