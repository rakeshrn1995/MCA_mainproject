# Generated by Django 2.1.5 on 2019-03-27 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0007_remove_regservant_blood_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regservant',
            name='date_of_joining',
            field=models.DateField(),
        ),
    ]
