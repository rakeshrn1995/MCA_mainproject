from django.db import models

# Create your models here.
from django.utils import timezone


class ActivityCategory(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

PAYMENT_CHOICES = (('yes', 'Yes'), ('no', 'No'))

class CampRegistration(models.Model):
    category_name = models.ForeignKey(ActivityCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    conduct_date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(default=timezone.now)
    location = models.TextField()
    payment = models.CharField(max_length=25, choices=PAYMENT_CHOICES)
    file = models.FileField(upload_to='campfiles/', blank=True)
    status = models.CharField(max_length=25, default='pending')

    def __str__(self):
        return self.name


from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class JobType(models.Model):
        jobtype = models.CharField(max_length=100)

        def __str__(self):
                return self.jobtype



GENDER_CHOICES = (('male', 'Male'), ('female', 'Female'))
class RegServant(models.Model):
        first_name = models.CharField(max_length=50)
        last_name = models.CharField(max_length=50)
        address = models.TextField(blank=True, null=False)
        dob = models.DateField(auto_now=False, auto_now_add=False)
        gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
        # blood_group = models.ForeignKey(BloodGrp, on_delete=models.CASCADE)
        job_type = models.ForeignKey(JobType, on_delete=models.CASCADE)
        date_of_joining = models.DateField(auto_now=False, auto_now_add=False)
        phone = models.CharField(max_length=10, blank=True, null=False)
        photo = models.ImageField(upload_to='profilepics/', blank=True, default='profilepics/default.jpg')
        status = models.IntegerField(default=1)
        def __str__(self):
            return self.first_name


class News(models.Model):
    heading = models.CharField(max_length=500)
    date = models.DateTimeField(default=timezone.now)
    detail = models.TextField()
    photo = models.ImageField(upload_to='newspics/', blank=True, default='newspics/default.png')

    def __str__(self):
        return self.heading