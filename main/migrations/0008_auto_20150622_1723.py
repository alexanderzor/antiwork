# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20150622_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='anonymous',
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 22, 14, 23, 31, 289566, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 22, 14, 23, 31, 291761, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='new',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 22, 14, 23, 31, 288156, tzinfo=utc)),
        ),
    ]
