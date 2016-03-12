# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=250)),
                ('fecha_pub', models.DateTimeField(auto_now_add=True)),
                ('cuerpo', models.TextField()),
                ('autor', models.ForeignKey(related_name='entradas_blog', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
