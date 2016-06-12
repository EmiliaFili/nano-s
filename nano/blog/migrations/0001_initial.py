# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('headline', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', verbose_name='Tags', through='taggit.TaggedItem', blank=True, to='taggit.Tag')),
            ],
            options={
                'db_table': 'nano_blog_entry',
                'verbose_name_plural': 'entries',
                'ordering': ('-pub_date',),
                'get_latest_by': 'pub_date',
            },
        ),
    ]
