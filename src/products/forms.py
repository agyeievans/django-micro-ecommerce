from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Product

input_css_class = "form-control"

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'handle', 'price']

    # designing form widget for all fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs['placeholder'] = "Your name"
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = input_css_class

class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image', 'name', 'handle', 'price']

    # designing form widget for all fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs['placeholder'] = "Your name"
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = input_css_class