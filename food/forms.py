#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm

from food.models import Comment
from food.models import Product

class LargeSearchForm(forms.Form):
    """
    Large search engine form on the home page
    """
    query = forms.CharField(label="", max_length=100)
    query.widget.attrs.update({
                    "id": "large-search-form",
                    "class": "form-control form-control-lg",
                    "type": "search",
                    "placeholder": "Produit",
                    "aria-label": "Recherche",
                })

    def clean_search(self):
        """
        Cleaning of received data
        """
        return self.cleaned_data['query']

class SmallSearchForm(forms.Form):
    """
    Small search engine for the navigation bar
    """
    query = forms.CharField(label="", max_length=100)
    query.widget.attrs.update({
                    "id": "small-search-form",
                    "class": "form-control form-control-lg",
                    "type": "search",
                    "placeholder": "Produit",
                    "aria-label": "Recherche",
                })

    def clean_search(self):
        """
        Cleaning of received data
        """
        return self.cleaned_data['query']
    

class CommentForm(forms.ModelForm):
    """
    Users can write a comment on a product detail sheet
    """
    class Meta:
        model = Comment
        fields = ('content')
