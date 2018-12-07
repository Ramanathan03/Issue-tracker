# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-06 22:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0011_auto_20181206_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_tickets_form',
            name='date_create',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='comment_form',
            name='comment_created',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]