# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0005_auto_20160312_0124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Discussion',
            new_name='discussion',
        ),
    ]
