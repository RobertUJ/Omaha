# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0021_auto_20160218_0102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainproject',
            name='user',
        ),
        migrations.AddField(
            model_name='mainproject',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
