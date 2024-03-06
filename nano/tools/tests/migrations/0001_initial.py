# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-10-21 11:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TreeItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(blank=True, default='', max_length=255)),
                ('part_of', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='has_treeitem_children', to='nano_tools_tests.TreeItem')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('tree', django.db.models.manager.Manager()),
            ],
        ),
    ]