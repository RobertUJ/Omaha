# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0004_auto_20160122_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designmodelrequest',
            name='asked_date',
            field=models.DateTimeField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='designmodelrequest',
            name='tentative_date',
            field=models.DateTimeField(max_length=100, null=True, blank=True),
        ),
    ]
