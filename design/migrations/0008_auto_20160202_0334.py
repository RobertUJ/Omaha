# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0007_auto_20160122_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designmodelrequest',
            name='user_assigner',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
