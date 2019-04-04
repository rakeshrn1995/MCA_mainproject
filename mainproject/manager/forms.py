from django import forms
from .models import RegServant


class SignUpServantForm(forms.ModelForm):

    class Meta:
        # widgets = {
        #     'date_of_joining': forms.DateInput(attrs={'class': 'datepicker'}),
        # }
        model = RegServant
        fields = '__all__'
        exclude = ['photo']

