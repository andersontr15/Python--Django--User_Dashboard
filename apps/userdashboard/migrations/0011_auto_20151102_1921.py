# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdashboard', '0010_poke_counter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poke',
            name='counter',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
