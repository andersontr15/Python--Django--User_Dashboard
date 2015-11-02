# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdashboard', '0008_remove_comment_receiver'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poke',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('poked', models.ForeignKey(related_name='poked', to='userdashboard.User', null=True)),
                ('poker', models.ForeignKey(related_name='poker', to='userdashboard.User', null=True)),
            ],
            options={
                'db_table': 'pokes',
            },
        ),
    ]
