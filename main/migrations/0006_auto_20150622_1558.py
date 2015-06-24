# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20150622_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 22, 12, 58, 59, 530851, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='company',
            field=models.ForeignKey(related_name='feedbacks', to='main.Company'),
        ),
        migrations.AlterField(
            model_name='new',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 22, 12, 58, 59, 529455, tzinfo=utc)),
        ),
    ]
