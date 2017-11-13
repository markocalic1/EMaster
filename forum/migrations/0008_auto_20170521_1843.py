# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-21 16:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_auto_20170521_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='stamp_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topic',
            name='stamp_updated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]