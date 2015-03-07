# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_project_last_modified'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('state', models.IntegerField(choices=[(0, b'Complete'), (1, b'Queued'), (2, b'Failed')])),
                ('number', models.IntegerField()),
                ('project', models.ForeignKey(to='project.Project')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
