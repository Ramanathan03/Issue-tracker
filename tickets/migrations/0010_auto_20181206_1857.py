# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-06 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0009_auto_20181206_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_tickets_form',
            name='priority',
            field=models.CharField(choices=[('HIGH', 'High'), ('LOW', 'Low')], default='Low', max_length=15),
        ),
    ]
