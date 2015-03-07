# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 7, 16, 31, 21, 239969, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
