# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=50)),
                ('description', models.TextField(default=b'', max_length=200, null=True)),
                ('justification', models.TextField(default=b'', max_length=200, null=True)),
                ('analysis', models.TextField(default=b'', max_length=200)),
            ],
        ),
    ]
