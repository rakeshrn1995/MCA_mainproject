# Generated by Django 2.1.5 on 2019-05-03 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0020_auto_20190406_1844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reguser',
            name='user_type',
        ),
    ]
