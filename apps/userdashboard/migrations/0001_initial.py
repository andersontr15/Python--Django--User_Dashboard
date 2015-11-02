# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField(max_length=200)),
                ('created_at', models.DateField(null=True)),
                ('updated_at', models.DateField()),
            ],
            options={
                'db_table': 'comments',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField(max_length=200)),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField()),
            ],
            options={
                'db_table': 'messages',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.TextField(max_length=20)),
                ('last_name', models.TextField(max_length=20)),
                ('email', models.TextField(max_length=20)),
                ('password', models.TextField(max_length=20)),
                ('user_level', models.IntegerField(null=True)),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField()),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(related_name='message_user', to='userdashboard.User'),
        ),
        migrations.AddField(
            model_name='comment',
            name='message',
            field=models.ForeignKey(related_name='comment_message', to='userdashboard.Message', null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(related_name='comment_user', to='userdashboard.User'),
        ),
    ]
