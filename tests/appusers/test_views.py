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
        self.login_url = reverse('login_url')
        self.registration_url = reverse('registration_url')
        self.logout_url = reverse('logout')
        self.dashboard_url = reverse('dashboard')
        self.favourites_url = reverse('substitutes')
        self.delete_favourites_url = reverse('delete_substitutes')
        self.user = User.objects.create_user(
            email='user@test.com',
            first_name='Nicolas',
            last_name='Martin',
            username='testuser',
            password='12test12',
            )
        self.user_ok = {
            'email': 'hop@test.com',
            'first_name': 'Laurent',
            'last_name': 'Dupond',
            'username': 'testuser',
            'password1': '85test102',
            'password2': '85test102',
        }
        self.user_unmatching_password = {
            'email': 'testemail@email.com',
            'first_name': 'Nicolas',
            'last_name': 'Martin',
            'username': 'test',
            'password1': '123hop456',
            'password2': '123hop456',
        }
        self.user_email_invalid = {
            'email': 'testemail.com',
            'first_name': 'Nicolas',
            'last_name': 'Martin',
            'username': 'test',
            'password1': '12test12',
            'password2': '12test12',
        }
        self.user_login_success = {
            'username': 'user@test.com',
            'password': '12test12'
        }
        self.user_login_unmatching_id = {
            'username': 'toto@test.com',
            'password': '12test12'
        }
        self.user_login_unmatching_password = {
            'username': 'user@test.com',
            'password': 'xxxxxxx'
        }
        
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
                nutriscore='B',
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
        
        self.created_substitute_pk = Substitute.objects.create(
            initial_product_id=self.created_product_pk1,
            substituted_product_id=self.created_product_pk2
        ).pk
        self.substitute = Substitute.objects.get(pk=self.created_substitute_pk)
        
        return super().setUp()

class RegistrationTest(BaseTest):

    def test_registration_success(self):
        response = self.client.post(self.registration_url, self.user_ok)
        self.assertEquals(response.status_code, 200)

    def test_registration_unmatching_password(self):
        response = self.client.post(self.registration_url, self.user_unmatching_password)
        self.assertEquals(response.status_code, 302)

    def test_registration_invalid_email(self):
        response = self.client.post(self.registration_url, self.user_email_invalid)
        self.assertEquals(response.status_code, 200)

class LoginTest(BaseTest):

    def test_login_sucess(self):
        response = self.client.post(self.login_url, self.user_login_success, follow=True)
        self.assertTrue(response.context['user'].is_active)

    def test_login_unmatching_id(self):
        response = self.client.post(self.login_url, self.user_login_unmatching_id, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertFalse(response.context['user'].is_active)

    def test_login_unmatching_password(self):
        response = self.client.post(self.login_url, self.user_login_unmatching_password, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertFalse(response.context['user'].is_active)

class SavedSubstitutesViewTest(BaseTest):
        
    def test_saved_substitutes_view_post(self):
        self.client.force_login(self.user)
        # response = self.client.post(self.delete_favourites_url, { 'substituteId': self.substitute.pk }, content_type='application/json')
        # self.assertEqual(response.status_code, 204)

class DeleteSubstitutesViewTest(BaseTest):
    
    def test_saved_substitutes_delete_favourite_success(self):
        self.client.force_login(self.user)
        response = self.client.post(self.delete_favourites_url, { 'substituteId': self.substitute.pk }, content_type='application/json')
        self.assertEqual(response.status_code, 204)
        
    def test_saved_substitutes_delete_favourite_bad_id(self):
        self.client.force_login(self.user)
        response = self.client.post(self.delete_favourites_url, { 'substituteId': 338 }, content_type='application/json')
        self.assertEqual(response.status_code, 404)
