from django.db import models

# Create your models here.

class ActivityCategory(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class CampRegistration(models.Model):
    category_name = models.ForeignKey(ActivityCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    conduct_date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField()
    location = models.CharField(max_length=300)
    file = models.FileField(upload_to='campfiles/', blank=True)
    status = models.CharField(max_length=25, default='Pending')

    def __str__(self):
        return self.type

