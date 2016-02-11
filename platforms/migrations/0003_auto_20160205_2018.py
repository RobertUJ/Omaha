# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platforms', '0002_auto_20160205_2004'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypesModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='platformsmodel',
            name='name',
        ),
        migrations.RemoveField(
            model_name='platformsmodel',
            name='priority',
        ),
    ]
