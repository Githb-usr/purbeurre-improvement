#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from food.models import Product
from users.models import User, Substitute

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
        
        return super().setUp()

class UrlsTest(BaseTest):
    def test_registration_url(self):
        response = self.client.get(reverse('registration_url'))
        self.assertTemplateUsed(response, 'users/registration.html')
        self.assertEquals(response.status_code, 200)
    
    def test_login_url(self):
        response = self.client.get(reverse('login_url'))
        self.assertTemplateUsed(response, 'users/login.html')
        self.assertEquals(response.status_code, 200)
    
    def test_dashboard_url(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('dashboard'))
        self.assertTemplateUsed(response, 'users/dashboard.html')
        self.assertEqual(response.status_code, 200)
        
    def test_dashboard_url_failed(self):
        # If you are not logged in to your account, you are redirected to the login page
        response = self.client.get(reverse('dashboard'))
        self.assertRedirects(response, '/user/login/?next=/user/dashboard/')
        self.assertEquals(response.status_code, 302)

    def test_saved_substitutes_url(self):
        # You log in to your account and then access a page that is only visible if you are logged in
        self.client.force_login(self.user)
        response = self.client.get(reverse('substitutes'))
        self.assertEqual(response.context['user'].username, 'testuser')
        self.assertTemplateUsed(response, 'users/my_substitutes.html')
        self.assertEqual(response.status_code, 200)
        
    def test_saved_substitutes_url_failed(self):
        # If you are not logged in to your account, you are redirected to the login page
        response = self.client.get(reverse('substitutes'))
        self.assertRedirects(response, '/user/login/?next=/user/my_substitutes/')
        self.assertEquals(response.status_code, 302)

    def test_delete_substitutes_url(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('delete_substitutes'))
        self.assertEqual(response.status_code, 301)
        
    def test_delete_substitutes_url_fail(self):
        response = self.client.get(reverse('delete_substitutes'))
        self.assertRedirects(response, '/user/login/?next=/user/delete_substitutes/')
        self.assertEqual(response.status_code, 302)
        
    def test_logout_url(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('logout'), follow=True)
        self.assertFalse(response.context['user'].is_active)
        self.assertTemplateUsed(response, 'users/login.html')
        self.assertEqual(response.status_code, 200)
