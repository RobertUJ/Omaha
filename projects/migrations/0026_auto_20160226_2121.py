# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0025_auto_20160226_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainproject',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
