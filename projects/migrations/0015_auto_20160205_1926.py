# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_auto_20160202_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainproject',
            name='platform',
            field=models.CharField(max_length=1),
        ),
    ]
