from django import forms
from .models import ActivityCategory, CampRegistration


class ActivityCategoryForm(forms.ModelForm):

    class Meta:
        model = ActivityCategory
        fields = ['category_name']

class CampForm(forms.ModelForm):
    class Meta:
        model = CampRegistration
        fields = '__all__'
        exclude = ['status']


