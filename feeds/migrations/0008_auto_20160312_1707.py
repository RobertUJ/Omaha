# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0007_remove_comment_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='discussion',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
