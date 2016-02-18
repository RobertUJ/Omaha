# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0020_mainproject_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainproject',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, blank=True),
        ),
    ]
