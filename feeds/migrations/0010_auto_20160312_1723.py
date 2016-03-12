# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0009_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='discussion',
        ),
        migrations.AddField(
            model_name='comment',
            name='discussion',
            field=models.ForeignKey(default=1, to='feeds.Discussion'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='discussion',
            name='category',
            field=models.CharField(default=b'projects', max_length=30, choices=[(b'projects', b'Proyectos'), (b'modules', b'Modulos'), (b'todos', b'Listas'), (b'tasks', b'Tareas'), (b'design', b'Dise\xc3\xb1o'), (b'docs', b'Documentos'), (b'tickesys', b'Tickets')]),
        ),
    ]
