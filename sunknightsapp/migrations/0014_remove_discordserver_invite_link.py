# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-26 16:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sunknightsapp', '0013_clanuserpreferences'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discordserver',
            name='invite_link',
        ),
    ]
