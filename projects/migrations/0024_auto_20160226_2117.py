# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0023_auto_20160226_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainproject',
            name='due_date',
            field=models.DateField(blank=True),
        ),
    ]
