# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-21 21:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20181021_2151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='username',
            new_name='user',
        ),
    ]
