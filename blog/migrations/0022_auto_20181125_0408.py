# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-11-25 04:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20181125_0332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.RemoveField(
            model_name='itemcomment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='itemcomment',
            name='item',
        ),
        migrations.AlterField(
            model_name='assignmentcomment',
            name='excel_sheet',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='ItemComment',
        ),
    ]
