# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20150201_1521'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='label',
            new_name='title',
        ),
    ]
