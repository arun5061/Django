# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-28 02:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_details', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='price',
            field=models.DecimalField(decimal_places=2, default=350, max_digits=1000),
        ),
    ]