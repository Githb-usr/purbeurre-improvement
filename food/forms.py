#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm

from food.models import Product

class SearchForm(forms.Form):
    """
        xxx
    """
    query = forms.CharField(label="", max_length=100)
    query.widget.attrs.update({
                    "class": "form-control form-control-lg",
                    "type": "search",
                    "placeholder": "Produit",
                    "aria-label": "Recherche",
                    "aria-describedby": "button-addon2"
                })
    
    def clean_search(self):
        """
            xxx
        """
        return self.cleaned_data['query']
