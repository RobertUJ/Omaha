# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0006_todolistmodel_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolistmodel',
            name='user_assigned',
        ),
    ]
