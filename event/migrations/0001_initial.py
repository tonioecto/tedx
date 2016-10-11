# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Intervenants',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=254, verbose_name=b'Nom de la stat-up')),
                ('description', models.TextField(verbose_name=b'Description', blank=True)),
                ('image', models.FileField(upload_to=b'startups', verbose_name=b'Image :')),
            ],
        ),
    ]
