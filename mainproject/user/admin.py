from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(BookCtg)
admin.site.register(BookDetail)
admin.site.register(MaintainType)
admin.site.register(MaintainRegister)