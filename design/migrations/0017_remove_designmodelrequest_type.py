# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0016_auto_20160205_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='designmodelrequest',
            name='type',
        ),
    ]
