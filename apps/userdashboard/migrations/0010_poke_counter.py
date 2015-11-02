# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdashboard', '0009_poke'),
    ]

    operations = [
        migrations.AddField(
            model_name='poke',
            name='counter',
            field=models.IntegerField(null=True),
        ),
    ]
