# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20160211_1701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='descripcion',
        ),
    ]
