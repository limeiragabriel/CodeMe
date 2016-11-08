# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activitie', '0007_question_is_done'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='quizImage',
        ),
    ]
