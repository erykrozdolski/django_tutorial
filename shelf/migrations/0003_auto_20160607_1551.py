# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-07 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0002_auto_20160607_1157'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ('last_name', 'first_name'), 'verbose_name': 'author', 'verbose_name_plural': 'authors'},
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=20, verbose_name='first name'),
        ),
    ]
