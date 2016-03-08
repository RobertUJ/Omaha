# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0020_designmailmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='designmodelresponse',
            name='file_type',
            field=models.CharField(default=b'1', max_length=4, choices=[(b'1', b'pdf'), (b'2', b'docx'), (b'3', b'image')]),
        ),
        migrations.AlterField(
            model_name='designmodelresponse',
            name='assignment',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
