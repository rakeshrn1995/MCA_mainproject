from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from login.models import RegUser
from .models import *


class ActivityCategoryForm(forms.ModelForm):

    class Meta:
        model = ActivityCategory
        fields = ['category_name']

class CampForm(forms.ModelForm):
    class Meta:
        model = CampRegistration
        fields = '__all__'
        exclude = ['status']

class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user

class RegUserForm(forms.ModelForm):
    class Meta:
        model = RegUser
        exclude = '__all__'
