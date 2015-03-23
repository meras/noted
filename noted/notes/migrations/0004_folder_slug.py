# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20150322_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='slug',
            field=models.SlugField(default=b' '),
            preserve_default=True,
        ),
    ]
