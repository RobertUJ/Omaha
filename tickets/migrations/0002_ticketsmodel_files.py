# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketsmodel',
            name='files',
            field=models.CharField(default=b'1', max_length=4),
        ),
    ]
