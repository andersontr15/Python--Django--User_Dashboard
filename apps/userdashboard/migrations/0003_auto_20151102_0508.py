# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdashboard', '0002_auto_20151102_0409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.TextField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.TextField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.TextField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.TextField(max_length=20, null=True),
        ),
    ]
