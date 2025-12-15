from django import forms
from django.forms import ModelForm
from django.core.validators import MinValueValidator, MaxValueValidator

from cars.models import Car

class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ["brand", "model", "year", "type", "price"]
        widgets = {
            'year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter year'}),
            "type": forms.Select(attrs={'class': 'form-select'}),
            "brand": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter brand name'}),
            "model": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter model name'}),
            "price": forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}),
            
        }
    