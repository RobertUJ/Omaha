# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_ticketsmodelresponse'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketsmodelresponse',
            name='ticket_status',
            field=models.ForeignKey(default=b'1', to='tickets.ticketsModel'),
        ),
    ]
