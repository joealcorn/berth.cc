# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20150303_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 7, 16, 31, 13, 691246, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
