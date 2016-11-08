# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activitie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='quizTitle',
            field=models.CharField(default=2, max_length=250),
            preserve_default=False,
        ),
    ]
