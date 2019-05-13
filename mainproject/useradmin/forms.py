from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from user.models import *
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

    def __init__(self, *args, **kwargs):
        super(CampForm, self).__init__(*args, **kwargs)
        self.fields['location'].widget.attrs['rows'] = 3

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


class SignUpServantForm(forms.ModelForm):

    class Meta:
        # widgets = {
        #     'date_of_joining': forms.DateInput(attrs={'class': 'datepicker'}),
        # }
        model = RegServant
        fields = '__all__'
        exclude = ['photo']

    def __init__(self, *args, **kwargs):
        super(SignUpServantForm, self).__init__(*args, **kwargs)
        self.fields['address'].widget.attrs['rows'] = 5




class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['heading', 'detail', 'photo']

class MaintainTypeForm(forms.ModelForm):

    class Meta:
        model = Type
        fields = ['type']

