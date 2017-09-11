# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-23 03:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellingPost', '0005_auto_20170822_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellingpost',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, blank = True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sellingpost',
            name='updated',
            field=models.DateTimeField(auto_now=True, blank = True),
        ),
    ]
