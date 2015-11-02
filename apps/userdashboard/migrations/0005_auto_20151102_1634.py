# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdashboard', '0004_auto_20151102_0527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
