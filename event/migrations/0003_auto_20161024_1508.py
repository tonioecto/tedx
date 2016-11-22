# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20161007_1113'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreviousSpeaker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=254, verbose_name=b'Nom du speaker')),
                ('description', models.TextField(verbose_name=b'Description', blank=True)),
                ('image', models.FileField(upload_to=b'media/speakers', verbose_name=b'Image :')),
                ('year', models.CharField(max_length=30, verbose_name=b'Annee ou le speaker est passe a tedx')),
            ],
        ),
        migrations.AlterField(
            model_name='speaker',
            name='image',
            field=models.FileField(upload_to=b'media/speakers', verbose_name=b'Image :'),
        ),
    ]
