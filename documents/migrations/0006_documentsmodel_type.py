# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0005_auto_20160209_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentsmodel',
            name='type',
            field=models.CharField(default=1, max_length=4, choices=[(b'1', b'pdf'), (b'2', b'Docx')]),
        ),
    ]
