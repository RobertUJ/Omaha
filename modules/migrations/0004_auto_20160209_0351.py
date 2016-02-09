# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0003_auto_20160206_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='analysis',
            field=models.TextField(default=b'', max_length=400),
        ),
        migrations.AlterField(
            model_name='module',
            name='description',
            field=models.TextField(default=b'', max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='justification',
            field=models.TextField(default=b'', max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
