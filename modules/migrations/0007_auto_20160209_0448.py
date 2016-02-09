# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0006_auto_20160209_0359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
