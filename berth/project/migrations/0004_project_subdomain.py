# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_project_last_modified'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='subdomain',
            field=models.CharField(default='default', unique=True, max_length=128),
            preserve_default=False,
        ),
    ]
