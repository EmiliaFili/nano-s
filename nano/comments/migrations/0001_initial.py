# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('path', models.CharField(default='', blank=True, max_length=255)),
                ('object_pk', models.TextField(verbose_name='object ID')),
                ('comment', models.TextField(max_length=3000)),
                ('comment_xhtml', models.TextField(editable=False)),
                ('added', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_visible', models.BooleanField(default=True)),
                ('is_scrambled', models.BooleanField(default=False)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', verbose_name='content type', related_name='content_type_set_for_comment')),
                ('part_of', models.ForeignKey(default=None, blank=True, to='comments.Comment', related_name='has_comment_children', null=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, related_name='comment_comments', null=True)),
            ],
            options={
                'get_latest_by': 'added',
                'ordering': ('added',),
                'db_table': 'nano_comments_comment',
            },
        ),
    ]
