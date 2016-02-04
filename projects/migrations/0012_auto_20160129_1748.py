# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_remove_mainproject_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mainproject',
            old_name='server_assigned',
            new_name='server',
        ),
    ]
