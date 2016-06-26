# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music_ACG',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('singer', models.CharField(max_length=100)),
                ('compose', models.CharField(max_length=100)),
                ('album', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=400)),
                ('label', models.CharField(max_length=500)),
                ('mark', models.CharField(max_length=100)),
                ('length', models.CharField(max_length=100)),
                ('lyrics', models.TextField()),
                ('url', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('listener', models.TextField()),
                ('comment', models.TextField()),
            ],
        ),
    ]
