# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0008_auto_20160202_0334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designmodelresponse',
            name='files',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
