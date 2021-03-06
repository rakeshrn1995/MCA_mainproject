# Generated by Django 2.1.5 on 2019-05-11 14:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


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
            name='CampRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('conduct_date', models.DateField()),
                ('time', models.TimeField()),
                ('location', models.CharField(max_length=300)),
                ('description', models.TextField(null=True)),
                ('file', models.FileField(blank=True, upload_to='campfiles/')),
                ('status', models.CharField(default='pending', max_length=25)),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useradmin.ActivityCategory')),
            ],
        ),
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobtype', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=500)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('detail', models.TextField()),
                ('photo', models.ImageField(blank=True, default='newspics/default.png', upload_to='newspics/')),
            ],
        ),
        migrations.CreateModel(
            name='RegServant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.TextField(blank=True)),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('date_of_joining', models.DateField()),
                ('phone', models.CharField(blank=True, max_length=10)),
                ('photo', models.ImageField(blank=True, default='profilepics/default.jpg', upload_to='profilepics/')),
                ('status', models.IntegerField(default=1)),
                ('job_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useradmin.JobType')),
            ],
        ),
    ]
