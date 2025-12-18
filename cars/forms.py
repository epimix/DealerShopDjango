from django import forms
from django.forms import ModelForm
from django.core.validators import MinValueValidator, MaxValueValidator

from cars.models import Car

class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ["brand", "model", "year", "type", "price","photo"]
        widgets = {
            "brand": forms.TextInput(attrs={
                "class": "block w-full rounded-xl border border-slate-300 bg-white px-3 py-2 text-sm shadow-sm "
                         "placeholder:text-slate-400 focus:border-blue-500 focus:ring-2 focus:ring-blue-200",
                "placeholder": "e.g. Toyota",
            }),
            "model": forms.TextInput(attrs={
                "class": "block w-full rounded-xl border border-slate-300 bg-white px-3 py-2 text-sm shadow-sm "
                         "placeholder:text-slate-400 focus:border-blue-500 focus:ring-2 focus:ring-blue-200",
                "placeholder": "e.g. Camry",
            }),
            "year": forms.NumberInput(attrs={
                "class": "block w-full rounded-xl border border-slate-300 bg-white px-3 py-2 text-sm shadow-sm "
                         "placeholder:text-slate-400 focus:border-blue-500 focus:ring-2 focus:ring-blue-200",
                "placeholder": "e.g. 2020",
                "min": "1900",
                "max": "2100",
            }),
            "type": forms.Select(attrs={
                "class": "block w-full rounded-xl border border-slate-300 bg-white px-3 py-2 text-sm shadow-sm "
                         "focus:border-blue-500 focus:ring-2 focus:ring-blue-200",
            }),
            "price": forms.NumberInput(attrs={
                "class": "block w-full rounded-xl border border-slate-300 bg-white px-3 py-2 text-sm shadow-sm "
                         "placeholder:text-slate-400 focus:border-blue-500 focus:ring-2 focus:ring-blue-200",
                "placeholder": "e.g. 24000",
                "min": "1",
                "step": "0.01",
            }),
            "photo": forms.ClearableFileInput(attrs={
                "class": "block w-full rounded-xl border border-slate-300 bg-white px-3 py-2 text-sm shadow-sm "
                         "file:mr-3 file:rounded-lg file:border-0 file:bg-slate-100 file:px-3 file:py-2 "
                         "file:text-sm file:font-semibold file:text-slate-700 hover:file:bg-slate-200",
            }),
        }
    