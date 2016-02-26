# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0009_module_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='name',
            field=models.CharField(default=b'', unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='module',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True, unique=True),
        ),
    ]
