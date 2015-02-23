# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default='test'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='note',
            name='tags',
            field=models.ManyToManyField(related_name='notes', to='notes.Tag', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tag',
            name='label',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
