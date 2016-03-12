# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feeds', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=250)),
                ('fecha_pub', models.DateTimeField(auto_now_add=True)),
                ('cuerpo', models.TextField()),
                ('autor', models.ForeignKey(related_name='entradas_blog', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Comment', models.ManyToManyField(to='feeds.Comment')),
            ],
        ),
        migrations.RemoveField(
            model_name='entrada',
            name='autor',
        ),
        migrations.DeleteModel(
            name='Entrada',
        ),
    ]
