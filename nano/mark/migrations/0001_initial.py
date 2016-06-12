# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('object_pk', models.TextField(verbose_name='object ID')),
                ('marked_at', models.DateTimeField(verbose_name='date/time marked', default=django.utils.timezone.now)),
                ('comment', models.CharField(blank=True, null=True, max_length=256)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', verbose_name='content type', related_name='content_type_set_for_mark')),
                ('marked_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='user', related_name='marks')),
            ],
            options={
                'ordering': ('marked_at',),
                'db_table': 'nano_mark',
                'get_latest_by': 'marked_at',
            },
        ),
        migrations.CreateModel(
            name='MarkType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=32)),
                ('slug', models.SlugField(unique=True)),
                ('hide', models.BooleanField(default=False)),
                ('verify', models.BooleanField(default=False)),
                ('permanent', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'nano_mark_marktype',
            },
        ),
        migrations.AddField(
            model_name='mark',
            name='marktype',
            field=models.ForeignKey(to='mark.MarkType'),
        ),
    ]
