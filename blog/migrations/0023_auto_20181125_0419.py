# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-11-25 04:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20181125_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignmentcomment',
            name='excel_sheet',
            field=models.FileField(blank=True, default='settings.MEDIA_ROOT/test.xls', null=True, upload_to=''),
        ),
    ]