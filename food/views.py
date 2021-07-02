#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import TemplateView, ListView

from food.database_service import DatabaseService
from food.forms import SearchForm
from users.forms import SavedSubstituteForm
from food.models import Product, Category, Store
from food.search_parser import SearchParser
from food.settings import NUTRIENT_LEVELS

def nav_search_form(request):
    """
        We display xxx
        :return: xxx
    """
    nav_search_form = SearchForm()
    
    return {
        "nav_search_form": nav_search_form,
    }
    
def show_index(request):
    """
        We display the home page of the site
        :return: index template
    """
    search_form = SearchForm()
    
    return render(request, 'index.html', { 'search_form': search_form })

def show_search_result(request):
    """
        xxx
        :return: xxxx
    """
    paginate_by = 6
    searchParser = SearchParser()
    # We get the product name entered by the user
    query = request.GET['query']
    
    # We parse the string sent by the user (we obtain a list of words)
    cleaned_query = searchParser.get_cleaned_string(query)

    # If there is at least 1 word
    if len(cleaned_query) > 0:
        # We look for matches with all the words
        for i in range(len(cleaned_query)):
            product_search_by_name = Product.objects.filter(designation__unaccent__icontains=cleaned_query[i])
            product_search_by_barcode = Product.objects.filter(barcode=cleaned_query[0])

            if len(product_search_by_name) == 1:
                nutriment_level_data = determine_nutriment_level_data(product_search_by_name[0])
                return render(request, 'product_detail.html', { 'product_detail': product_search_by_name[0], 'nutriment_data': nutriment_level_data, 'query': query })
            # If there are any matches, we send them to the template
            elif len(product_search_by_name) > 1:
                return render(request, 'product_list.html', { 'product_search_result': product_search_by_name, 'query': query })
            # If the user has entered a very specific product name or barcode, and there is only one result
            elif product_search_by_barcode:
                nutriment_level_data = determine_nutriment_level_data(product_search_by_barcode[0])
                return render(request, 'product_detail.html', { 'product_detail': product_search_by_barcode[0], 'nutriment_data': nutriment_level_data, 'query': query })

            return render(request, 'product_list.html', { 'product_search_result': 'NO_DATA', 'query': query })
        
def show_product_detail(request, barcode):
    """
        xxx
        :param barcode: xxx
        :return: xxxx
    """
    product_detail = Product.objects.get(barcode=barcode)
    nutriment_level_data = determine_nutriment_level_data(product_detail)

    return render(request, 'product_detail.html', {
        'product_detail': product_detail,
        'nutriment_data': nutriment_level_data
        })

def show_substitute_choice_list(request, barcode):
    """
        xxx
        :param field_string: xxx
        :return: xxxx
    """
    hidden_form = SavedSubstituteForm()
    
    initial_product = Product.objects.get(barcode=barcode)
    initial_product_categories = initial_product.categories.all()
    substitute_search = Product.objects.filter(categories__in=initial_product_categories)\
                        .filter(nutriscore__lt=initial_product.nutriscore)\
                        .order_by('nutriscore').distinct()

    if substitute_search:
        return render(request, 'substitute_list.html', {
            'initial_product': initial_product,
            'substitute_search_result': substitute_search,
            "hidden_form": hidden_form,
            })

    return render(request, 'substitute_list.html', {
        'initial_product': initial_product,
        'substitute_search_result': 'NO_DATA'
        })

def determine_level_data(level):
    """
        xxx
        :param product: xxx
        :return: xxxx
    """
    level_data = {}
    if level == 'LO':
        level_data['color'] = 'green-dot'
        level_data['quantity'] = 'faible quantité'
    elif level =='MO':
        level_data['color'] = 'orange-dot'
        level_data['quantity'] = 'quantité modérée'
    elif level =='HI':
        level_data['color'] = 'red-dot'
        level_data['quantity'] = 'quantité élevée'

    return level_data

def determine_nutriment_level_data(product):
    """
        xxx
        :param product: xxx
        :return: xxxx
    """
    nutriment_level_data = {}
    if product.fat_level:
        nutriment_level_data['fat'] = determine_level_data(product.fat_level)
    
    if product.fat_level:
        nutriment_level_data['saturated_fat'] = determine_level_data(product.saturated_fat_level)
    
    if product.fat_level:
        nutriment_level_data['sugars'] = determine_level_data(product.sugars_level)
    
    if product.fat_level:
        nutriment_level_data['salt'] = determine_level_data(product.salt_level)

    return nutriment_level_data
