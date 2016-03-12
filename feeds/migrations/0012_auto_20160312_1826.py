# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feeds', '0011_comment_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
                ('author', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DiscussionModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_category', models.IntegerField(null=True)),
                ('category', models.CharField(default=b'projects', max_length=30, choices=[(b'projects', b'Proyectos'), (b'modules', b'Modulos'), (b'todos', b'Listas'), (b'tasks', b'Tareas'), (b'design', b'Dise\xc3\xb1o'), (b'docs', b'Documentos'), (b'tickesys', b'Tickets')])),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='discussion',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Discussion',
        ),
        migrations.AddField(
            model_name='commentmodel',
            name='discussion',
            field=models.ForeignKey(to='feeds.DiscussionModel'),
        ),
    ]
