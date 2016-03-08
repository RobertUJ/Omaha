# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_remove_ticketsmodel_files'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketsmodel',
            name='files',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
    ]
