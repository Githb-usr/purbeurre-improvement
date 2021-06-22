#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Product, Category, Store

class ProductAdmin(admin.ModelAdmin):
    """
        xxx
    """
    list_display = ('designation', 'brand', 'barcode', 'nutriscore',
                    'fat_value', 'fat_levels',
                    'saturated_fat_value', 'saturated_fat_levels',
                    'sugars_value', 'sugars_levels',
                    'salt_value', 'salt_levels',
                    'url', 'image_url')
    
class CategoryAdmin(admin.ModelAdmin):
    """
        xxx
    """
    list_display = ('designation',)
    
class StoreAdmin(admin.ModelAdmin):
    """
        xxx
    """
    list_display = ('designation',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Store, StoreAdmin)
