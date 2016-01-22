# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0003_designmodelrequest_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designmodelrequest',
            name='asked_date',
            field=models.DateField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='designmodelrequest',
            name='tentative_date',
            field=models.DateField(max_length=100, null=True, blank=True),
        ),
    ]
