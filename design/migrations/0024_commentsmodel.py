# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0023_auto_20160218_2321'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentsModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(max_length=500, null=True, blank=True)),
                ('request', models.ForeignKey(to='design.DesignModelRequest')),
                ('response', models.ForeignKey(to='design.DesignModelResponse')),
            ],
        ),
    ]
