# Generated by Django 2.1.7 on 2019-11-07 14:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0005_auto_20190701_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricesraw',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date'),
        ),
    ]
