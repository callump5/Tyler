# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-20 23:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tyler_site', '0006_auto_20181021_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='client',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
