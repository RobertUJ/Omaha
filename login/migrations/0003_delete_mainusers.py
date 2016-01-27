# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20160121_2036'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MainUsers',
        ),
    ]
