# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-24 14:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log_reg', '0001_initial'),
        ('travels', '0002_auto_20180323_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='createor',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='log_reg.User'),
        ),
    ]
