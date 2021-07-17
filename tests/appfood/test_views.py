#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model
from django.test import Client, SimpleTestCase, TestCase
from django.urls import reverse

from food.forms import SmallSearchForm, LargeSearchForm
from food.models import Product, Category
from food.views import determine_level_data, determine_nutriment_level_data
from users.models import User

class BaseTest(TestCase):
    def setUp(self):
        # Set up non-modified objects used by all test methods
        User = get_user_model()
        self.user = User.objects.create_user(
            email='user@test.com',
            first_name='Nicolas',
            last_name='Martin',
            username='testuser',
            password='12test12',
            )

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

        self.category1 = Category.objects.create(designation='Biscuits au chocolat')
        self.category2 = Category.objects.create(designation='Produits à tartiner sucrés')
        
        self.category1.products.add(Product.objects.get(barcode=8000500310427))
        self.category1.products.add(Product.objects.get(barcode=7613034626844))
        self.category2.products.add(Product.objects.get(barcode=8000500310427))
        self.category2.products.add(Product.objects.get(barcode=7613034626844))
        
        return super().setUp()

class IndexPageTestCase(BaseTest):
    def test_index_page(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)

class ProductDetailPageTestCase(BaseTest):
    def test_product_detail_page_returns_200(self):
        response = self.client.get(reverse('product_detail', args=(self.initial_product.barcode,)))
        self.assertEqual(response.status_code, 200)

    def test_product_detail_page_returns_404(self):
        response = self.client.get(reverse('product_detail', args=(self.initial_product.designation,)))
        self.assertEqual(response.status_code, 404)

class SearchResultPageTestCase(BaseTest):
    def test_search_result_name_success(self):
        response = self.client.post('/product_list/?query=chocapic')
        self.assertNotEqual(response.context['search_result'], 'NO_DATA')
        self.assertEqual(response.status_code, 200)

    def test_search_result_barcode_success(self):
        response = self.client.post('/product_list/?query=8000500310427')
        self.assertNotEqual(response.context['search_result'], 'NO_DATA')
        self.assertEqual(response.status_code, 200)

    def test_search_result_no_product(self):
        response = self.client.post('/product_list/?query=chaise')
        self.assertEqual(response.context['search_result'], 'NO_DATA')
        self.assertEqual(response.status_code, 200)

    def test_search_result_blank_request(self):
        response = self.client.post('/product_list/?query=    ')
        self.assertEqual(response.context['search_result'], 'NO_DATA')
        self.assertEqual(response.status_code, 200)

class SubstituteListPageTestCase(BaseTest):
    def test_substitute_list_page_post_returns_200(self):
        response = self.client.get(reverse('substitute_list', args=(self.initial_product.barcode,)))
        self.assertNotEqual(response.context['search_result'], 'NO_DATA')
        self.assertEqual(response.status_code, 200)

    def test_substitute_list_page_post_returns_404(self):
        response = self.client.get(reverse('substitute_list', args=(self.initial_product.designation,)))
        self.assertEqual(response.status_code, 404)

    def test_substitute_list_page_nutriscore_A(self):
        response = self.client.get(reverse('substitute_list', args=(self.substituted_product.barcode,)))
        self.assertEqual(response.context['search_result'], 'NO_DATA')
        self.assertEqual(response.status_code, 200)

class DetermineLevelDataTestCase(BaseTest):
    def test_determine_level_data_lo(self):
        result = determine_level_data('LO')
        self.assertEqual(result, { 'color': 'green-dot', 'quantity': 'faible quantité'})

    def test_determine_level_data_mo(self):
        result = determine_level_data('MO')
        self.assertEqual(result, { 'color': 'orange-dot', 'quantity': 'quantité modérée'})

    def test_determine_level_data_hi(self):
        result = determine_level_data('HI')
        self.assertEqual(result, { 'color': 'red-dot', 'quantity': 'quantité élevée'})

class DetermineNutrimentLevelDataTestCase(BaseTest):
    def determine_nutriment_level_data(self):
        result = determine_nutriment_level_data(self.initial_product)
        self.assertEqual(result, {
            'fat': { 'color': 'red-dot', 'quantity': 'quantité élevée'},
            'saturated_fat': { 'color': 'red-dot', 'quantity': 'quantité élevée'},
            'sugars': { 'color': 'red-dot', 'quantity': 'quantité élevée'},
            'salt': { 'color': 'orange-dot', 'quantity': 'quantité modérée'},
            })
