# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20150622_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 22, 13, 47, 14, 249175, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 22, 13, 47, 14, 246912, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='new',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 22, 13, 47, 14, 245474, tzinfo=utc)),
        ),
    ]
