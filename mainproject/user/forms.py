from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from login.models import RegUser
from login import config
from django.db.models import Q
from .models import *
from useradmin.forms import *



class MemRegForm(forms.ModelForm):

    class Meta:
        model = MemReg
        fields = ['username', 'first_name', 'last_name', 'dob', 'gender', 'blood_group', 'job', 'photo']

    def __init__(self, *args, **kwargs):
        super(MemRegForm, self).__init__(*args, **kwargs)
        #self.fields['username'].widget.attrs['disabled'] = True
        self.fields['username'].empty_label = None
        self.fields['username'].queryset = User.objects.filter(username=config.username)


class BookDetailForm(forms.ModelForm):
    class Meta:
        model = BookDetail
        fields = ['username', 'category_name', 'book_name', 'author', 'language', 'description', 'image', 'book_file']
        labels = {
            "username": "Username",
            "category_name": "Category type",
            "book_name": "Book name",
            "author": "Author",
            "language": "Language",
            "description": "Description",
            "image": "Image",
            "book_file": "Add Book File",

            }
        exclude = ['status']

    def __init__(self, *args, **kwargs):
        super(BookDetailForm, self).__init__(*args, **kwargs)
        #self.fields['username'].widget.attrs['disabled'] = True
        self.fields['username'].empty_label = None
        self.fields['username'].queryset = User.objects.filter(username=config.username)
        self.fields['language'].queryset = Language.objects.filter(~Q(id = 5))
        #Entry.objects.filter(~Q(date = 2006))
        self.fields['description'].widget.attrs['rows'] = 5




class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['email']

class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = RegUser
        fields = ['job', 'phone', 'photo']


class MaintainForm(forms.ModelForm):
    class Meta:
        model = MaintainRegister
        fields = '__all__'
        exclude = ['status', 'requested_date', 'solved_date']

    def __init__(self, *args, **kwargs):
        super(MaintainForm, self).__init__(*args, **kwargs)
        #self.fields['username'].widget.attrs['disabled'] = True
        self.fields['username'].empty_label = None
        self.fields['username'].queryset = User.objects.filter(username=config.username)
        self.fields['description'].widget.attrs['rows'] = 5





class ServantReqForm(forms.ModelForm):
    class Meta:
        model = ServantRequest
        fields = ['username', 'job', 'servant', 'request_date', 'day_choice', 'description']
        labels = {
            "username": "Username",
            "job": "Job Type",
            "servant": "Servant",
            "request_date": "Choose Date",
            "day_choice": "Choose Time",
            "description": "Description",
        }


    def __init__(self, *args, **kwargs):
        super(ServantReqForm, self).__init__(*args, **kwargs)
        #self.fields['username'].widget.attrs['disabled'] = True
        self.fields['username'].empty_label = None
        self.fields['username'].queryset = User.objects.filter(username=config.username)
        self.fields['description'].widget.attrs['rows'] = 5


class BookList_Form(forms.ModelForm):
    class Meta:
        model = BookDetail
        fields = ['language']

    def __init__(self, *args, **kwargs):
        super(BookList_Form, self).__init__(*args, **kwargs)
        #self.fields['username'].widget.attrs['disabled'] = True
        self.fields['language'].empty_label = None
        #self.fields['username'].queryset = User.objects.filter(username=config.username)
        #self.fields['description'].widget.attrs['rows'] = 5


class MemberList_Form(forms.ModelForm):
    class Meta:
        model = MemReg
        fields = '__all__'


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        # if self.fields['first_name'] == :
        #     self.fields['first_name'].widget.attrs['disabled'] = True
        # if self.fields['last_name']:
        #     self.fields['last_name'].widget.attrs['disabled'] = True

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = RegUser
        fields = ['dob', 'gender', 'blood_group', 'house_name', 'house_number', 'job', 'phone', 'photo']

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        # if self.fields['dob']:
        #     self.fields['dob'].widget.attrs['disabled'] = True
        # if self.fields['gender']:
        #     self.fields['gender'].widget.attrs['disabled'] = True
        # if self.fields['blood_group']:
        #     self.fields['blood_group'].widget.attrs['disabled'] = True

