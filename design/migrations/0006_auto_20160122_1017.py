# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0005_auto_20160122_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designmodelresponse',
            name='coment',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
