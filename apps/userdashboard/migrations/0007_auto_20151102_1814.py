# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdashboard', '0006_user_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='receiver',
            field=models.ForeignKey(related_name='receiver_comment_user', to='userdashboard.User', null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='sender',
            field=models.ForeignKey(related_name='sender_comment_user', to='userdashboard.User', null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(related_name='receiver_message_user', to='userdashboard.User', null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(related_name='sender_message_user', to='userdashboard.User', null=True),
        ),
    ]
