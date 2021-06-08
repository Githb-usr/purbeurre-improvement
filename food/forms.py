#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.forms import ModelForm

from food.models import Product

class FoodForm(ModelForm):
    """
        xxx
    """
    class Meta:
        model = Product
        fields = ['designation', 'brand', 'barcode', 'nutriscore', 'novascore', 'url']
