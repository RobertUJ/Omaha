# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0006_documentsmodel_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentsmodel',
            name='type',
            field=models.CharField(default=2, max_length=4, choices=[(b'1', b'pdf'), (b'2', b'Docx')]),
        ),
    ]
