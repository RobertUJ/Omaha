# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_remove_userprofile_comentario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='photo',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='descripcion',
            field=models.TextField(default=b'', max_length=200, blank=True),
        ),
    ]
