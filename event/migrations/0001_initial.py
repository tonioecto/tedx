# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-29 22:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email')),
            ],
        ),
        migrations.CreateModel(
            name='PreviousSpeaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, verbose_name='Nom du speaker')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('resume', models.CharField(blank=True, max_length=254, verbose_name='Une description rapide')),
                ('image', models.FileField(upload_to='assets/media/media/speakers', verbose_name='Image :')),
                ('year', models.CharField(max_length=30, verbose_name='Annee ou le speaker est passe a tedx')),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, verbose_name='Nom du speaker')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('resume', models.CharField(blank=True, max_length=254, verbose_name='Une description rapide')),
                ('image', models.FileField(upload_to='assets/media/media/speakers', verbose_name='Image :')),
                ('heure', models.CharField(blank=True, max_length=100, verbose_name='Heure de passage')),
            ],
        ),
    ]
