# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-13 21:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boundaries', '0002_country_iso_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='boundaries.State'),
        ),
    ]
