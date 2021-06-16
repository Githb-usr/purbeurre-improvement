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
        xxx
        :param field_string: xxx
        :return: xxxx
        :rtype: xxx
    """
    search_form = SearchForm()
    
    return render(request, 'index.html', { 'form': search_form })

def show_search_form(request):
    """
        xxx
        :param field_string: xxx
        :return: xxxx
        :rtype: xxx
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
    query = request.GET['query']
    cleaned_query = searchParser.get_cleaned_string(query)

    if len(cleaned_query) > 0:
        for i in range(len(cleaned_query)):
            product_search_by_name = Product.objects.filter(designation__unaccent__icontains=cleaned_query[i])

        if product_search_by_name:
            return render(request, 'product_list.html', { 'product_search_result': product_search_by_name })

        product_search_by_barcode = Product.objects.filter(barcode__icontains=cleaned_query[0])
        if product_search_by_barcode:
            return render(request, 'product_list.html', { 'product_search_result': product_search_by_barcode })
