# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('activitie', '0002_quiz_quiztitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='description',
            field=models.CharField(default=datetime.datetime(2016, 10, 12, 17, 32, 40, 390297, tzinfo=utc), max_length=500),
            preserve_default=False,
        ),
    ]
