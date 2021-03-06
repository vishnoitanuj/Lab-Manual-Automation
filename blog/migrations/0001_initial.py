# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-16 14:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('desciption', models.CharField(max_length=500)),
                ('profile_image', models.FileField(blank=True, null=True, upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.FileField(blank=True, null=True, upload_to=b'')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('draft', models.BooleanField(default=False)),
                ('publish', models.DateField()),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Author')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
