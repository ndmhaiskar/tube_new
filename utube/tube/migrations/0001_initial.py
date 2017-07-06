# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VideoUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('vfile', models.FileField(upload_to='media')),
                ('category', models.CharField(max_length=100)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
    ]
