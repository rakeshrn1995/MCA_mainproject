# Generated by Django 2.1.5 on 2019-03-26 06:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_auto_20190326_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regservant',
            name='date_of_joining',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
