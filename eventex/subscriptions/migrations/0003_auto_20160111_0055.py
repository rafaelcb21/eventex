# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-11 02:55
from __future__ import unicode_literals

from django.db import migrations, models
import eventex.subscriptions.models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0002_auto_20160108_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='key_hash',
            field=models.CharField(default=eventex.subscriptions.models.hash_, max_length=40, verbose_name='hash'),
        ),
    ]
