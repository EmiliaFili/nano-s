# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-10-20 13:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveIntegerField(default=100)),
                ('name', models.CharField(max_length=20, unique=True)),
                ('description', models.TextField()),
                ('receivers', models.ManyToManyField(blank=True, related_name='badges', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'nano_badge_badge',
            },
        ),
    ]
