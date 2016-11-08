# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activitie', '0004_question_a'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='a',
            new_name='Questiontext',
        ),
    ]
