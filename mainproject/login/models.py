from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# class login(models.Model):
#     usnm = models.CharField(max_length=50)
#     pswd = models.CharField(max_length=50)
from django.urls import reverse

GENDER_CHOICES = (('male', 'Male'), ('female', 'Female'))
TYPE_CHOICES = (('user', 'User'), ('manager', 'Manager'))


class BloodGrp(models.Model):
    blood_grp = models.CharField(max_length=10)

    def __str__(self):
        return self.blood_grp


class RegUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    blood_group = models.ForeignKey(BloodGrp, on_delete=models.CASCADE)
    job = models.CharField(max_length=50, blank=True, null=False)
    house_name = models.CharField(max_length=100, blank=True, null=False)
    house_number = models.CharField(max_length=50, blank=True, null=False)
    phone = models.CharField(max_length=10, blank=True, null=False)
    user_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='user')
    photo = models.ImageField(upload_to='profilepics/', blank=True, null=True, default='default.jpg')

    def get_absolute_url(self):
        return reverse()
    def __str__(self):
        return self.user.username

class ActivityCtg(models.Model):
    ctg_name = models.CharField(max_length=200)

