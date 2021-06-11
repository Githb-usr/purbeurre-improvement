#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

class Product(models.Model):
    """
        xxx
    """
    designation = models.CharField(max_length=250)
    brand = models.CharField(max_length=60)
    barcode = models.CharField(max_length=13)
    nutriscore = models.CharField(max_length=1)
    novascore = models.CharField(max_length=1)
    url = models.URLField(max_length=200)
    image_url = models.URLField(max_length=150)
    
    def __str__(self):
        return self.designation
    
    class Meta:
        verbose_name_plural = "products"

class Category(models.Model):
    """
        xxx
    """
    designation = models.CharField(max_length=150, unique=True)
    products = models.ManyToManyField(Product, related_name='categories')
    
    def __str__(self):
        return self.designation
    
    class Meta:
        verbose_name_plural = "categories"

class Store(models.Model):
    """
        xxx
    """
    designation = models.CharField(max_length=200, unique=True)
    products = models.ManyToManyField(Product, related_name='stores')
    
    def __str__(self):
        return self.designation
    
    class Meta:
        verbose_name_plural = "stores"
