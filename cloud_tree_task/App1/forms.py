from django import forms
from .models import StudentModels

class Studentform(forms.ModelForm):
    class Meta:
        model=StudentModels
        fields="__all__"