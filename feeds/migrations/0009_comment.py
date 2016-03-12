# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0008_auto_20160312_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
                ('discussion', models.ManyToManyField(to='feeds.Discussion')),
            ],
        ),
    ]
