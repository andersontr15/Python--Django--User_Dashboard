# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdashboard', '0007_auto_20151102_1814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='receiver',
        ),
    ]
