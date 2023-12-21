from django import forms
from django.core.validators import MinValueValidator

from .models import Producto

class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={'class':'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-indigo-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-indigo-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'}
        ),
        required=True,
    )
    
    precio = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class':'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-indigo-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-indigo-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'},
        ), 
        required=True,
    )
    
    cantidad = forms.CharField(
        widget=forms.NumberInput(
            attrs={'class':'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-indigo-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-indigo-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'}
        ),
        required=True,
    )
    
    class Meta:
        model = Producto
        fields = ["nombre", "precio", "cantidad"]

class ActualizarProductoForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(
        attrs={'class':'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6'}
        ), required=True)
    
    precio = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class':'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6'}
        ), 
        required=True,
    )
    
    cantidad = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class':'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6'}
        ),
        required=True,
    )
    
    class Meta:
        model = Producto
        fields = ["nombre", "precio", "cantidad"]