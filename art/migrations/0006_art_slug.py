# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-16 03:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0005_auto_20161002_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='slug',
            field=models.SlugField(default='one-off', help_text='Suggested value automatically generated from title. Must be unique.'),
            preserve_default=False,
        ),
    ]
