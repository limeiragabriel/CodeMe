# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activitie', '0005_auto_20161018_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='quizImage',
            field=models.CharField(default='a', max_length=1000),
            preserve_default=False,
        ),
    ]
