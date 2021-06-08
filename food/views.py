#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, redirect

from food.database_service import DatabaseService
from food.forms import FoodForm
from food.models import Product, Category, Store

def index(request):
    """
        xxx
        :param field_string: xxx
        :return: xxxx
        :rtype: xxx
    """
    # récupérer tous les produits de la BDD
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})
    # return HttpResponse("Hello, world. You're at the food index.")

def import_products(request):
    """
        xxx
        :param field_string: xxx
        :return: xxxx
        :rtype: xxx
    """
    database_service = DatabaseService()
    database_service.get_api_data()
    all_products = database_service.populate_database_with_products()
    all_categories = database_service.populate_database_with_categories()
    database_service.populate_database_with_category_products()
    all_stores = database_service.populate_database_with_stores()
    database_service.populate_database_with_store_products()

    return render (request, 'showallproducts.html', { "all_products": all_products } )
