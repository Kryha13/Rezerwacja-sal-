# Generated by Django 2.1.7 on 2019-02-18 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_auto_20190218_1853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booked',
            name='room',
        ),
        migrations.DeleteModel(
            name='Booked',
        ),
    ]
