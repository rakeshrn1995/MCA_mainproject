from django.db import models
# from login.models import BloodGrp


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
        age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
        gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
        # blood_group = models.ForeignKey(BloodGrp, on_delete=models.CASCADE)
        job_type = models.ForeignKey(JobType, on_delete=models.CASCADE)
        date_of_joining = models.DateField(auto_now=False, auto_now_add=False)
        photo = models.ImageField(upload_to='profilepics/', blank=True, null=True, default='default.jpg')

        def __str__(self):
            return self.first_name


