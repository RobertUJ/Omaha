# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0017_remove_designmodelrequest_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='designmodelrequest',
            name='platform',
        ),
        migrations.RemoveField(
            model_name='designmodelresponse',
            name='platform',
        ),
        migrations.RemoveField(
            model_name='designmodelresponse',
            name='type',
        ),
    ]
