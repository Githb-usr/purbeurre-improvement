#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.test import Client, TestCase
from django.urls import reverse

from food.models import Product

class BaseTest(TestCase):
    def setUp(self):
        # Set up non-modified objects used by all test methods
        self.created_product_pk1 = Product.objects.create(
                designation='Nutella biscuits',
                barcode='8000500310427',
                brand='Ferrero',
                nutriscore='E',
                fat_value='24.5',
                fat_level='HI',
                saturated_fat_value='11.8',
                saturated_fat_level='HI',
                sugars_value='34.7',
                sugars_level='HI',
                salt_value='0.529',
                salt_level='MO',
                url='https://fr.openfoodfacts.org/produit/8000500310427/nutella-biscuits-ferrero',
                image_url='https://static.openfoodfacts.org/images/products/800/050/031/0427/front_fr.97.400.jpg'
                ).pk
        self.initial_product = Product.objects.get(pk=self.created_product_pk1)

        self.created_product_pk2 = Product.objects.create(
                designation='Chocapic',
                barcode='7613034626844',
                brand='Nestlé',
                nutriscore='A',
                fat_value='4.6',
                fat_level='MO',
                saturated_fat_value='1.3',
                saturated_fat_level='LO',
                sugars_value='25',
                sugars_level='HI',
                salt_value='0.22',
                salt_level='LO',
                url='https://fr.openfoodfacts.org/produit/7613034626844/chocapic-nestle',
                image_url='https://static.openfoodfacts.org/images/products/761/303/462/6844/front_fr.184.400.jpg'
                ).pk
        self.substituted_product = Product.objects.get(pk=self.created_product_pk2)
        
        return super().setUp()

class UrlsTest(BaseTest):
    def test_homepage_url(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)
    
    def test_product_list_url(self):
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)
    
    def test_product_detail_url(self):
        response = self.client.get(reverse('product_detail', args=(self.initial_product.barcode,)))
        self.assertEqual(response.status_code, 200)
    
    def test_substitute_list_url(self):
        response = self.client.get(reverse('substitute_list', args=(self.substituted_product.barcode,)))
        self.assertEqual(response.status_code, 200)