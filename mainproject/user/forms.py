from django import forms
from django.contrib.auth.models import User

from login.models import RegUser
from login import config
from .models import *



class MemRegForm(forms.ModelForm):

    class Meta:
        model = MemReg
        fields = ['username', 'first_name', 'last_name', 'age', 'gender', 'blood_group', 'job' ]

    def __init__(self, *args, **kwargs):
        super(MemRegForm, self).__init__(*args, **kwargs)
        #self.fields['username'].widget.attrs['disabled'] = True
        self.fields['username'].empty_label = None
        self.fields['username'].queryset = User.objects.filter(username=config.username)


class BookDetailForm(forms.ModelForm):
    class Meta:
        model = BookDetail
        fields = ['username', 'category_name', 'book_name', 'author', 'language', 'description', 'book_file']
        labels = {
            "username": "Username",
            "category_name": "Category type",
            "book_name": "Book name",
            "author": "Author",
            "language": "Language",
            "description": "Description",
            "book_file": "Add Book File",

            }
        exclude = ['status']

    def __init__(self, *args, **kwargs):
        super(BookDetailForm, self).__init__(*args, **kwargs)
        #self.fields['username'].widget.attrs['disabled'] = True
        self.fields['username'].empty_label = None
        self.fields['username'].queryset = User.objects.filter(username=config.username)


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
        exclude = ['status']

    def __init__(self, *args, **kwargs):
        super(MaintainForm, self).__init__(*args, **kwargs)
        #self.fields['username'].widget.attrs['disabled'] = True
        self.fields['username'].empty_label = None
        self.fields['username'].queryset = User.objects.filter(username=config.username)



class ServantReqForm(forms.ModelForm):
    class Meta:
        model = ServantRequest
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ServantReqForm, self).__init__(*args, **kwargs)
        #self.fields['username'].widget.attrs['disabled'] = True
        self.fields['username'].empty_label = None
        self.fields['username'].queryset = User.objects.filter(username=config.username)