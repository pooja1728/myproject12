# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-17 05:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_auto_20170917_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantlocation',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
