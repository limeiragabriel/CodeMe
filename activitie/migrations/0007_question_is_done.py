# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activitie', '0006_quiz_quizimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='is_Done',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
