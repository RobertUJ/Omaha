# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_userprofile_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='password',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='username',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
