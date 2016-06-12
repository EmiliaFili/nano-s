# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PM',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('text', models.TextField()),
                ('text_formatted', models.TextField(editable=False)),
                ('text_type', models.CharField(max_length=64, default='plaintext')),
                ('subject', models.CharField(max_length=64, default='', blank=True)),
                ('sent', models.DateTimeField(editable=False, default=django.utils.timezone.now)),
                ('sender_deleted', models.BooleanField(default=False)),
                ('recipient_archived', models.BooleanField(default=False)),
                ('recipient_deleted', models.BooleanField(default=False)),
                ('recipient', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='pms_received')),
                ('sender', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='pms_sent')),
            ],
            options={
                'db_table': 'nano_privmsg_pm',
            },
        ),
    ]
