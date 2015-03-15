# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_auto_20150307_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='state',
            field=models.IntegerField(choices=[(0, b'Complete'), (1, b'Queued'), (2, b'Failed'), (3, b'In Progress')]),
            preserve_default=True,
        ),
    ]
