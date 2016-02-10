# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_auto_20160202_2054'),
        ('design', '0012_auto_20160202_0533'),
    ]

    operations = [
        migrations.AddField(
            model_name='designmodelrequest',
            name='project',
            field=models.ManyToManyField(to='projects.MainProject'),
        ),
        migrations.AddField(
            model_name='designmodelresponse',
            name='project',
            field=models.ManyToManyField(to='projects.MainProject'),
        ),
    ]
