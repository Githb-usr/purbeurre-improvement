#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.test import TestCase

from food.models import Product, Category, Store
from food.views import show_product_detail

class ProductModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.prod_id = Product.objects.create(
            designation='Pains au lait',
            barcode='3256540000698',
            brand='Brioche Pasquier',
            nutriscore='D',
            fat_value='13',
            fat_level='MO',
            saturated_fat_value='4.6',
            saturated_fat_level='MO',
            sugars_value='11',
            sugars_level='MO',
            salt_value='1.1',
            salt_level='MO',
            url='https://fr.openfoodfacts.org/produit/3256540000698/pains-au-lait-pasquier',
            image_url='https://static.openfoodfacts.org/images/products/325/654/000/0698/front_fr.126.400.jpg'
            ).pk
    
    def test_designation_label(self):
        product = Product.objects.get(id=self.prod_id)
        field_label = product._meta.get_field('designation').verbose_name
        self.assertEquals(field_label, 'designation')
        
    def test_barcode_label(self):
        product = Product.objects.get(id=self.prod_id)
        field_label = product._meta.get_field('barcode').verbose_name
        self.assertEquals(field_label, 'barcode')
        
    def test_brand_label(self):
        product = Product.objects.get(id=self.prod_id)
        field_label = product._meta.get_field('brand').verbose_name
        self.assertEquals(field_label, 'brand')
        
    def test_nutriscore_label(self):
        product = Product.objects.get(id=self.prod_id)
        field_label = product._meta.get_field('nutriscore').verbose_name
        self.assertEquals(field_label, 'nutriscore')
        
    def test_fat_value_label(self):
        product = Product.objects.get(id=self.prod_id)
        field_label = product._meta.get_field('fat_value').verbose_name
        self.assertEquals(field_label, 'fat value')

    def test_fat_level_label(self):
        product = Product.objects.get(id=self.prod_id)
        field_label = product._meta.get_field('fat_level').verbose_name
        self.assertEquals(field_label, 'fat level')
        
    def test_saturated_fat_value_label(self):
        product = Product.objects.get(id=self.prod_id)
        field_label = product._meta.get_field('saturated_fat_value').verbose_name
        self.assertEquals(field_label, 'saturated fat value')
        
    def test_saturated_fat_level_label(self):
        product = Product.objects.get(id=self.prod_id)
        field_label = product._meta.get_field('saturated_fat_level').verbose_name
        self.assertEquals(field_label, 'saturated fat level')
        
    def test_sugars_value_label(self):
        product = Product.objects.get(id=self.prod_id)
        field_label = product._meta.get_field('sugars_value').verbose_name
        self.assertEquals(field_label, 'sugars value')
        
    def test_sugars_level_label(self):
        product = Product.objects.get(id=self.prod_id)
        field_label = product._meta.get_field('sugars_level').verbose_name
        self.assertEquals(field_label, 'sugars level')

    def test_salt_value_label(self):
        product = Product.objects.get(id=self.prod_id)
        field_label = product._meta.get_field('salt_value').verbose_name
        self.assertEquals(field_label, 'salt value')
        
    def test_salt_level_label(self):
        product = Product.objects.get(id=self.prod_id)
        field_label = product._meta.get_field('salt_level').verbose_name
        self.assertEquals(field_label, 'salt level')
        
    def test_url_label(self):
        product = Product.objects.get(id=self.prod_id)
        field_label = product._meta.get_field('url').verbose_name
        self.assertEquals(field_label, 'url')
        
    def test_image_url_label(self):
        product = Product.objects.get(id=self.prod_id)
        field_label = product._meta.get_field('image_url').verbose_name
        self.assertEquals(field_label, 'image url')
        
    def test_substitutes_label(self):
        product = Product.objects.get(id=self.prod_id)
        field_label = product._meta.get_field('substitutes').verbose_name
        self.assertEquals(field_label, 'substitutes')
          
    def test_designation_max_length(self):
        product = Product.objects.get(id=self.prod_id)
        max_length = product._meta.get_field('designation').max_length
        self.assertEquals(max_length, 250)
        
    def test_barcode_max_length(self):
        product = Product.objects.get(id=self.prod_id)
        max_length = product._meta.get_field('barcode').max_length
        self.assertEquals(max_length, 13)
        
    def test_brand_max_length(self):
        product = Product.objects.get(id=self.prod_id)
        max_length = product._meta.get_field('brand').max_length
        self.assertEquals(max_length, 60)
        
    def test_nutriscore_max_length(self):
        product = Product.objects.get(id=self.prod_id)
        max_length = product._meta.get_field('nutriscore').max_length
        self.assertEquals(max_length, 1)
        
    def test_fat_level_max_length(self):
        product = Product.objects.get(id=self.prod_id)
        max_length = product._meta.get_field('fat_level').max_length
        self.assertEquals(max_length, 2)
        
    def test_saturated_fat_level_max_length(self):
        product = Product.objects.get(id=self.prod_id)
        max_length = product._meta.get_field('saturated_fat_level').max_length
        self.assertEquals(max_length, 2)
        
    def test_sugars_level_max_length(self):
        product = Product.objects.get(id=self.prod_id)
        max_length = product._meta.get_field('sugars_level').max_length
        self.assertEquals(max_length, 2)
        
    def test_salt_level_max_length(self):
        product = Product.objects.get(id=self.prod_id)
        max_length = product._meta.get_field('salt_level').max_length
        self.assertEquals(max_length, 2)
        
    def test_url_max_length(self):
        product = Product.objects.get(id=self.prod_id)
        max_length = product._meta.get_field('url').max_length
        self.assertEquals(max_length, 200)
        
    def test_image_url_max_length(self):
        product = Product.objects.get(id=self.prod_id)
        max_length = product._meta.get_field('image_url').max_length
        self.assertEquals(max_length, 150)

    def test_object_name_is_designation(self):
        product = Product.objects.get(id=self.prod_id)
        expected_object_name = product.designation
        self.assertEquals(expected_object_name, str(product))

    def test_get_absolute_url(self):
        product = Product.objects.get(id=self.prod_id)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(product.get_absolute_url(), '/product_detail/3256540000698/')

class CategoryModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.cat_id = Category.objects.create(
            designation='Pâtes à tartiner aux noisettes'
            ).pk

    def test_designation_max_length(self):
        category = Category.objects.get(id=self.cat_id)
        max_length = category._meta.get_field('designation').max_length
        self.assertEquals(max_length, 150)

    def test_object_name_is_designation(self):
        category = Category.objects.get(id=self.cat_id)
        expected_object_name = category.designation
        self.assertEquals(expected_object_name, str(category))

class StoreModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.store_id = Store.objects.create(
            designation='Carrefour'
            ).pk

    def test_designation_max_length(self):
        store = Store.objects.get(id=self.store_id)
        max_length = store._meta.get_field('designation').max_length
        self.assertEquals(max_length, 200)

    def test_object_name_is_designation(self):
        store = Store.objects.get(id=self.store_id)
        expected_object_name = store.designation
        self.assertEquals(expected_object_name, str(store))
