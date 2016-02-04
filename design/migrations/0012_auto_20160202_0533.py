# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0011_auto_20160202_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designmodelresponse',
            name='files',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
    ]
