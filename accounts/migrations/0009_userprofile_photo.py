# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20160205_0033'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'UserProfile', blank=True),
        ),
    ]
