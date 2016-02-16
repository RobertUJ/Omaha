# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0010_auto_20160215_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentsmodel',
            name='files',
            field=models.FileField(null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='documentsmodel',
            name='images',
            field=models.FileField(null=True, upload_to=b''),
        ),
    ]
