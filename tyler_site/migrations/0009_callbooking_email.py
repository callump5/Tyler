# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-21 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tyler_site', '0008_callbooking'),
    ]

    operations = [
        migrations.AddField(
            model_name='callbooking',
            name='email',
            field=models.CharField(default='qfq', max_length=300),
            preserve_default=False,
        ),
    ]