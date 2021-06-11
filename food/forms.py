#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm

from food.models import Product

class SearchForm(forms.Form):
    """
        xxx
    """
    query = forms.CharField(label='Votre recherche de produit', help_text="Saisissez le nom d'un produit", max_length=100)
    query.widget.attrs.update({
                    "class": "search_field",
                })
    
    def clean_search(self):
        """
            xxx
        """
        return self.cleaned_data['query']
    

class FoodForm(ModelForm):
    """
        xxx
    """
    class Meta:
        model = Product
        fields = ['designation', 'brand', 'barcode', 'nutriscore', 'novascore', 'url']
