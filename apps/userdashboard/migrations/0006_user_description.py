# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdashboard', '0005_auto_20151102_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
