# Generated by Django 2.1.5 on 2019-04-06 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MedcampRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('conduct_date', models.DateField()),
                ('time', models.TimeField()),
                ('location', models.CharField(max_length=300)),
                ('doc_name', models.CharField(max_length=200)),
                ('doc_contact', models.CharField(max_length=15)),
                ('status', models.CharField(max_length=25)),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useradmin.ActivityCategory')),
            ],
        ),
    ]
