# Generated by Django 2.1.7 on 2019-07-01 20:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0004_auto_20190701_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricesraw',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 1, 23, 33, 55, 570335), verbose_name='date'),
        ),
    ]
