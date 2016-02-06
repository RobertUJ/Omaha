# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0002_auto_20160205_2257'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Modules',
            new_name='Module',
        ),
    ]
