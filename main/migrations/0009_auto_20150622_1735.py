# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20150622_1723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 22, 14, 35, 13, 467934, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 22, 14, 35, 13, 470091, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='new',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 22, 14, 35, 13, 466366, tzinfo=utc)),
        ),
    ]
