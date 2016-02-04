# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import design.models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0010_auto_20160202_0428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designmodelresponse',
            name='files',
            field=models.ImageField(null=True, upload_to=design.models.url, blank=True),
        ),
    ]
