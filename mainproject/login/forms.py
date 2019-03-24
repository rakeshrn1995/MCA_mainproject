from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import RegUser, MemReg

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',  'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)

        if commit:
            user.save()
        return user

class RegUserForm(forms.ModelForm):


    class Meta:
        model = RegUser
        fields = ['age', 'gender', 'blood_group', 'job', 'house_name', 'house_number', 'phone', 'user_type', 'photo']


class MemRegForm(forms.ModelForm):

    class Meta:
        model = MemReg
        fields = ['first_name', 'last_name', 'age', 'gender', 'blood_group', 'job', 'photo']


