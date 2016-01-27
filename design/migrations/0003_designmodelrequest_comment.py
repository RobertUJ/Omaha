# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0002_auto_20160122_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='designmodelrequest',
            name='comment',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
