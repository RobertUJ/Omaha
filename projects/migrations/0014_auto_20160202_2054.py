# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_auto_20160202_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainproject',
            name='due_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='mainproject',
            name='start_date',
            field=models.DateField(),
        ),
    ]
