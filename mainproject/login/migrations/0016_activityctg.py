# Generated by Django 2.1.5 on 2019-04-04 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0015_auto_20190327_2355'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityCtg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctg_name', models.CharField(max_length=200)),
            ],
        ),
    ]
