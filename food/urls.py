#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_index, name='homepage'),
    path('product_list/', views.show_search_result, name='product_list'),
    path('product_list<str:query>', views.show_search_result, name='product_list'),
]