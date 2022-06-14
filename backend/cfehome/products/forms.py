from django import forms

from .models import *

class ProductForm(forms.ModelForm):
    class meta:
        model=Product
        fields='__all__'