# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_auto_20160208_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentsmodel',
            name='name',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
    ]
