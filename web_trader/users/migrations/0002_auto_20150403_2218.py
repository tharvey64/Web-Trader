# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
<<<<<<< HEAD
            field=models.CharField(unique=True, max_length=40),
            preserve_default=True,
=======
            field=models.CharField(max_length=40, unique=True),
>>>>>>> ff53f5d960066ea0208d4ad09682dca29f71ef2c
        ),
    ]
