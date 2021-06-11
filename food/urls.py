#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_index_view, name='homepage'),
    path('product_list/', views.get_search_result, name='product_list'),
    path('product_list<str:query>', views.get_search_result, name='product_list'),
]