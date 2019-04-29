from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)

        if commit:
            user.save()
        return user

class RegUserForm(forms.ModelForm):


    class Meta:
        model = RegUser
        fields = ['age', 'gender', 'blood_group',  'house_name', 'house_number', 'job', 'phone', 'user_type']





