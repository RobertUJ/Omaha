# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0021_auto_20160216_2324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='designmodelresponse',
            name='file_type',
        ),
        migrations.AlterField(
            model_name='designmodelresponse',
            name='assignment',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
