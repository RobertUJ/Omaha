# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20160308_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasksmodel',
            name='user_assigner',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
