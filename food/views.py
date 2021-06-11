#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView

from food.database_service import DatabaseService
from food.forms import SearchForm
from food.models import Product, Category, Store

def get_index_view(request):
    """
        xxx
        :param field_string: xxx
        :return: xxxx
        :rtype: xxx
    """
    search_form = SearchForm()
    
    return render(request, 'index.html', { 'form': search_form })

def get_search_view(request):
    """
        xxx
        :param field_string: xxx
        :return: xxxx
        :rtype: xxx
    """
    search_form = SearchForm()
    
    return render(request, 'index.html', { 'form': search_form })

def get_search_result(request):
    """
        xxx
        :param field_string: xxx
        :return: xxxx
        :rtype: xxx
    """
    query = request.GET['query']
    product_search = Product.objects.filter(designation__unaccent__icontains=query)
    brand_search = Product.objects.filter(brand__unaccent__icontains=query)
    category_search = Category.objects.filter(designation__unaccent__icontains=query)
    
    return render(request, 'product_list.html', { 
                                                 'product_search': product_search,
                                                 'brand_search': brand_search,
                                                 'category_search': category_search
                                                }
                  )
