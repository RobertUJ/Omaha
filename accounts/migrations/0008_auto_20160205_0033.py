# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20160204_2312'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='comment',
            new_name='comentario',
        ),
    ]
