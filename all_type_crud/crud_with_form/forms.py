from django import forms
from .models import CrudWithForm

class CrudForm(forms.ModelForm):
    category_name=forms.CharField(max_length=50,widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    category_code=forms.CharField(max_length=50,widget=forms.NumberInput(attrs={
        'class':'form-control'
    }))

    category_description=forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'rows':'5',
        'cols':'5'
    }))
    choices=(('Active','Active'),('Inactive','Inactive'))
    category_status=forms.CharField(widget=forms.Select(choices=choices,attrs={
        'class':'form-control'
    }))

    class Meta:
        model=CrudWithForm
        fields="__all__"