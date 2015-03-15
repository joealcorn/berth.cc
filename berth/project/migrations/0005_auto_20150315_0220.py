# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_project_subdomain'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='repo_identifier',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='repo_source',
            field=models.PositiveSmallIntegerField(default=0, choices=[(0, b'Github')]),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='project',
            unique_together=set([('repo_identifier', 'repo_source')]),
        ),
    ]
