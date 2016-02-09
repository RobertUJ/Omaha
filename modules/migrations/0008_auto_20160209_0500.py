# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0007_auto_20160209_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
