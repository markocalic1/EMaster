# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-21 12:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20170521_1439'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='topic_message',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='subject',
            new_name='new_title',
        ),
    ]