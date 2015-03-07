# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_auto_20150307_1805'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='job',
            unique_together=set([('project', 'number')]),
        ),
    ]
