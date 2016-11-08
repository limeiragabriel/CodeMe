# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activitie', '0003_question_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='a',
            field=models.TextField(default='a'),
            preserve_default=False,
        ),
    ]
