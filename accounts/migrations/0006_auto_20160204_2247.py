# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20160204_0122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='photo',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='comment',
            field=models.TextField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
