# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-11-25 04:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20181125_0421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignmentcomment',
            name='excel_sheet',
            field=models.FileField(blank=True, default='test.xlsx', null=True, upload_to=''),
        ),
    ]
