# Generated by Django 2.1.5 on 2019-03-22 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_auto_20190322_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='memreg',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='profilepics/'),
        ),
    ]
