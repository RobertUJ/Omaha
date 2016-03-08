# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0009_auto_20160208_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolistmodel',
            name='due_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='todolistmodel',
            name='name',
            field=models.CharField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='todolistmodel',
            name='start_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
