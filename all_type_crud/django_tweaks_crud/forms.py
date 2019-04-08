from django import forms
from .models import CrudWithTweaks
class CrudWithTweaksForm(forms.ModelForm):
    class Meta:
        model=CrudWithTweaks
        fields="__all__"