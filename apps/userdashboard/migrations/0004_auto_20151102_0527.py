# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdashboard', '0003_auto_20151102_0508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='updated_at',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='updated_at',
            field=models.DateField(null=True),
        ),
    ]
