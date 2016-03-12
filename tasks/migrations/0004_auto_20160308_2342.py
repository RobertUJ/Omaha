# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_tasksmodel_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasksmodel',
            name='due_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='tasksmodel',
            name='start_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='tasksmodel',
            name='user_assigned',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tasksmodel',
            name='user_assigner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
