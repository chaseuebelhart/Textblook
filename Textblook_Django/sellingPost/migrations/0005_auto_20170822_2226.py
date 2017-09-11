# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-23 03:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellingPost', '0004_auto_20170813_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellingpost',
            name='condition',
            field=models.CharField(choices=[('Used with markings', 'Used with markings'), ('Used with minimal/no markings', 'Used with minimal/no markings'), ('New', 'New')], default='New', max_length=31),
        ),
    ]