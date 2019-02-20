# Generated by Django 2.1.7 on 2019-02-18 18:08

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20190218_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='booked_from',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='room',
            name='booked_to',
            field=models.DateField(default=datetime.datetime(2019, 2, 18, 18, 8, 10, 709914, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
