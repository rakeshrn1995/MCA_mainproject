# Generated by Django 2.1.5 on 2019-03-26 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_auto_20190326_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regservant',
            name='date_of_joining',
            field=models.DateField(auto_now=True),
        ),
    ]
