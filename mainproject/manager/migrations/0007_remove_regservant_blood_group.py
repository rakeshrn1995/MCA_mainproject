# Generated by Django 2.1.5 on 2019-03-26 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0006_auto_20190326_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regservant',
            name='blood_group',
        ),
    ]
