# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fake_user_id', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('vegetarian', models.BooleanField(default=False)),
                ('vegan', models.BooleanField(default=False)),
                ('diabetes', models.BooleanField(default=False)),
                ('lactose_intolerance', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
