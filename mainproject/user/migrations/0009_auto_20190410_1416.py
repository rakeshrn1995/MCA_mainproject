# Generated by Django 2.1.5 on 2019-04-10 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20190410_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookdetail',
            name='image',
            field=models.ImageField(blank=True, default='bookicon.png', upload_to='bookfiles/'),
        ),
        migrations.AlterField(
            model_name='memreg',
            name='photo',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profilepics/'),
        ),
    ]
