# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0004_auto_20160310_2357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discussion',
            name='Comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='Discussion',
            field=models.ManyToManyField(to='feeds.Discussion'),
        ),
        migrations.AddField(
            model_name='discussion',
            name='id_category',
            field=models.IntegerField(null=True),
        ),
    ]
