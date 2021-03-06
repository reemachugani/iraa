# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-20 03:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0008_auto_20170619_0407'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='art_category',
            options={'ordering': ['category'], 'verbose_name': 'Art Category', 'verbose_name_plural': 'Art Categories'},
        ),
        migrations.AddField(
            model_name='art',
            name='client_name',
            field=models.CharField(blank=True, help_text='Max 250 characters', max_length=250, null=True),
        ),
    ]
