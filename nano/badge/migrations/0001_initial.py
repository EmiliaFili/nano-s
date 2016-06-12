# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('level', models.PositiveIntegerField(default=100)),
                ('name', models.CharField(max_length=20, unique=True)),
                ('description', models.TextField()),
                ('receivers', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='badges', blank=True)),
            ],
            options={
                'db_table': 'nano_badge_badge',
            },
        ),
    ]
