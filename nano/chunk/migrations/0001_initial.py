# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-10-20 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chunk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('content', models.TextField()),
            ],
            options={
                'db_table': 'nano_chunk_chunk',
            },
        ),
    ]
