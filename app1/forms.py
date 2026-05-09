from django import forms
from . models import Products


class products_form(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['product_name', 'price', 'quantity', 'size', 'colors']