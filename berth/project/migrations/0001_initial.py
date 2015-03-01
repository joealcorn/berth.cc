# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=128)),
                ('slug', models.CharField(unique=True, max_length=128)),
                ('repo_url', models.CharField(max_length=256)),
                ('owner', models.ForeignKey(to='user.User')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
