# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateField(null=True),
        ),
    ]
