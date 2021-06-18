#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView

from food.database_service import DatabaseService
from food.forms import SearchForm
from food.models import Product, Category, Store
from food.search_parser import SearchParser

def show_index(request):
    """
        We display the home page of the site
        :return: index template
    """
    search_form = SearchForm()

    return render(request, 'index.html', { 'form': search_form })

def show_search_form(request):
    """
        We instantiate the product search form to send it to the template
        :return: index template
    """
    search_form = SearchForm()

    return render(request, 'index.html', { 'form': search_form })

def show_search_result(request):
    """
        xxx
        :param field_string: xxx
        :return: xxxx
        :rtype: xxx
    """
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

        # If there are any matches, we send them to the template
        if product_search_by_name:
            return render(request, 'product_list.html', { 'product_search_result': product_search_by_name })

        # If the user has entered a very specific product name or barcode, and there is only one result
        product_search_by_barcode = Product.objects.filter(barcode__icontains=cleaned_query[0])
        if product_search_by_barcode:
            return render(request, 'product_list.html', { 'product_search_result': product_search_by_barcode })
        
def show_product_detail(self, request):
    """
        xxx
        :param field_string: xxx
        :return: xxxx
        :rtype: xxx
    """
    product_detail = Product.objects.filter(designation__unaccent__icontains="xxx")
    
    return render(request, 'product_detail.html', { 'product_detail': product_detail })

def show_substitute_choice_list(self, request):
    """
        xxx
        :param field_string: xxx
        :return: xxxx
        :rtype: xxx
    """
    substitute_search = Product.objects.filter(designation__unaccent__icontains="xxx")
    
    return render(request, 'substitute_list.html', { 'substitute_search_result': substitute_search })
