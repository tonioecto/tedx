# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-07 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, verbose_name=b'Nom du speaker')),
                ('description', models.TextField(blank=True, verbose_name=b'Description')),
                ('image', models.FileField(upload_to=b'speaker', verbose_name=b'Image :')),
            ],
        ),
        migrations.DeleteModel(
            name='Intervenants',
        ),
    ]