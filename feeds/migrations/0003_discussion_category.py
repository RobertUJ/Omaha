# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0002_auto_20160310_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussion',
            name='category',
            field=models.CharField(max_length=30, null=True, choices=[(b'projects', b'Proyectos'), (b'modules', b'Modulos'), (b'todos', b'Listas'), (b'tasks', b'Tareas'), (b'design', b'Dise\xc3\xb1o'), (b'docs', b'Documentos'), (b'tickesys', b'Tickets')]),
        ),
    ]
