# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-07 22:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bet_app', '0006_remove_bet_bet_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mybets',
            name='bet_taken',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bet_app.Bet'),
        ),
    ]
