#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Product, Category, Store

class ProductAdmin(admin.ModelAdmin):
    """
        Display of products in the back office
    """
    list_display = ('designation', 'brand', 'barcode', 'nutriscore',
                    'fat_value', 'fat_level',
                    'saturated_fat_value', 'saturated_fat_level',
                    'sugars_value', 'sugars_level',
                    'salt_value', 'salt_level',
                    'url', 'image_url')

class CategoryAdmin(admin.ModelAdmin):
    """
        Display of categories in the back office
    """
    list_display = ('designation',)

class StoreAdmin(admin.ModelAdmin):
    """
        Display of stores in the back office
    """
    list_display = ('designation',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Store, StoreAdmin)
