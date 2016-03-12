# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0003_discussion_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='autor',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='cuerpo',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='fecha_pub',
            new_name='date_pub',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='titulo',
            new_name='title',
        ),
    ]
