# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-19 13:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_delete_author'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TextModel',
        ),
    ]
