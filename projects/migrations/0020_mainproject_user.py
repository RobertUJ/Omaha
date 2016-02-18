# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0019_remove_mainproject_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainproject',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
