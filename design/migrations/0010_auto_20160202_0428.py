# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0009_auto_20160202_0356'),
    ]

    operations = [
        migrations.RenameField(
            model_name='designmodelresponse',
            old_name='coment',
            new_name='comment',
        ),
        migrations.AlterField(
            model_name='designmodelresponse',
            name='assignment',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='designmodelresponse',
            name='user_assigner',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
