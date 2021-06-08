#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('addproduct', views.create_product, name='addproduct'),
    path('showallproducts', views.import_products, name='showallproducts'),
    # on ajoute une 2ème ligne avec même url mais pouvant avoir des paramètres
    # path('addproduct/<int:id_product>', views.create_product, name='addproduct'),
]