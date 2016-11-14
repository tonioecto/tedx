# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_auto_20161106_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='heure',
            field=models.CharField(max_length=100, verbose_name=b'Heure de passage', blank=True),
        ),
    ]
