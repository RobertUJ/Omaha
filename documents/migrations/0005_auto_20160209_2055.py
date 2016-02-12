# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0004_auto_20160208_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentsmodel',
            name='name',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
