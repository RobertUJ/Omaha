# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0008_auto_20160209_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentsmodel',
            name='type',
            field=models.CharField(max_length=4, choices=[(b'1', b'pdf'), (b'2', b'docx'), (b'3', b'png'), (b'4', b'jpg'), (b'5', b'gif')]),
        ),
    ]
