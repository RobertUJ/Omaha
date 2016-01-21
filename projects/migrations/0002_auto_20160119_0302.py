# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mainproject',
            old_name='project_client',
            new_name='client',
        ),
        migrations.RenameField(
            model_name='mainproject',
            old_name='project_domain',
            new_name='domain',
        ),
        migrations.RenameField(
            model_name='mainproject',
            old_name='project_end_date',
            new_name='end_date',
        ),
        migrations.RenameField(
            model_name='mainproject',
            old_name='project_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='mainproject',
            old_name='project_platform',
            new_name='platform',
        ),
        migrations.RenameField(
            model_name='mainproject',
            old_name='project_priority',
            new_name='priority',
        ),
        migrations.RenameField(
            model_name='mainproject',
            old_name='project_server_assigned',
            new_name='server_assigned',
        ),
        migrations.RenameField(
            model_name='mainproject',
            old_name='project_start_date',
            new_name='start_date',
        ),
        migrations.RenameField(
            model_name='mainproject',
            old_name='project_type',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='mainproject',
            old_name='project_url',
            new_name='url',
        ),
        migrations.RenameField(
            model_name='mainproject',
            old_name='project_users',
            new_name='users',
        ),
    ]
