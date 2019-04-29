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

    def __init__(self, *args, **kwargs):
        super(SignUpServantForm, self).__init__(*args, **kwargs)
        self.fields['address'].widget.attrs['rows'] = 5
