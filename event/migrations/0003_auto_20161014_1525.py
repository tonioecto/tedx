# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20161007_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='image',
            field=models.FileField(upload_to=b'media/speakers', verbose_name=b'Image :'),
        ),
    ]
