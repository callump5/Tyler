# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-23 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tyler_site', '0014_auto_20181023_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(max_length=300),
        ),
    ]
