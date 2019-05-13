from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# class login(models.Model):
#     usnm = models.CharField(max_length=50)
#     pswd = models.CharField(max_length=50)
from django.urls import reverse

GENDER_CHOICES = (('male', 'Male'), ('female', 'Female'))



class BloodGrp(models.Model):
    blood_grp = models.CharField(max_length=10)

    def __str__(self):
        return self.blood_grp


class RegUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    blood_group = models.ForeignKey(BloodGrp, on_delete=models.CASCADE, default=2)
    job = models.CharField(max_length=50, blank=True,)
    house_name = models.CharField(max_length=100, blank=True )
    house_number = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=10, blank=True )
    photo = models.ImageField(upload_to='profilepics/', blank=True, default='profilepics/default.jpg')

    def get_absolute_url(self):
        return reverse()
    def __str__(self):
        return self.user.username

class ActivityCtg(models.Model):
    ctg_name = models.CharField(max_length=200)

