from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from login.models import BloodGrp
from useradmin.models import JobType
from useradmin.models import RegServant, CampRegistration
# Create your models here.


GENDER_CHOICES = (('male', 'Male'), ('female', 'Female'))
DAY_CHOICES = (('full', 'Full Day'), ('half', 'Half Day'))
# LANG_CHOICES = (('english', 'English'), ('malayalam', 'Malayalam'), ('hindi', 'Hindi'))


class MemReg(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    blood_group = models.ForeignKey(BloodGrp, on_delete=models.CASCADE)
    job = models.CharField(max_length=50, blank=True, null=False)
    photo = models.ImageField(upload_to='profilepics/', blank=True, default='profilepics/default.jpg')
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.username)

class BookCtg(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class Language(models.Model):
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.language

class BookDetail(models.Model):
    category_name = models.ForeignKey(BookCtg, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    description = models.TextField()
    book_file = models.FileField(upload_to='bookfiles/')
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='bookfiles/', blank=True, default='bookfiles/bookicon.png')
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.book_name

    # def get_absolute_url(self):
    #     return reverse('user:detail', kwargs={'pk': self.pk})


class Type(models.Model):
    type = models.CharField(max_length=100)
    def __str__(self):
        return self.type


class MaintainRegister(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    subject = models.CharField(max_length=500)
    description = models.TextField(null=True)
    requested_date = models.DateField(default=timezone.now)
    solved_date = models.DateField(null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.subject

class ServantRequest(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(JobType, on_delete=models.CASCADE)
    servant = models.ForeignKey(RegServant, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    request_date = models.DateField(auto_now=False, auto_now_add=False)
    day_choice = models.CharField(max_length=20, choices=DAY_CHOICES)
    description = models.TextField(null=True)
    status = models.CharField(max_length=50, default='pending')

    def __str__(self):
        return self.job

class CampRegister(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    camp_name = models.ForeignKey(CampRegistration, on_delete=models.CASCADE)
