#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
import json

from food.models import Product
from tests.config import INITIAL_PRODUCT_DATA_1, INITIAL_PRODUCT_DATA_2, SUBSTITUTED_PRODUCT_DATA_1, SUBSTITUTED_PRODUCT_DATA_2
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
        
        self.created_product_pk1 = Product.objects.create(**INITIAL_PRODUCT_DATA_1).pk
        self.initial_product_1 = Product.objects.get(pk=self.created_product_pk1)
        
        self.created_product_pk2 = Product.objects.create(**SUBSTITUTED_PRODUCT_DATA_1).pk
        self.substituted_product_1 = Product.objects.get(pk=self.created_product_pk2)
        
        self.created_product_pk3 = Product.objects.create(**INITIAL_PRODUCT_DATA_2).pk
        self.initial_product_2 = Product.objects.get(pk=self.created_product_pk3)
        
        self.created_product_pk4 = Product.objects.create(**SUBSTITUTED_PRODUCT_DATA_2).pk
        self.substituted_product_2 = Product.objects.get(pk=self.created_product_pk4)
        
        self.created_substitute_pk = Substitute.objects.create(
            initial_product_id=self.initial_product_2.pk,
            substituted_product_id=self.substituted_product_2.pk
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
        form_data = {'initial-product-id': self.initial_product_1.pk, 'substituted-product-id': self.substituted_product_1.pk}
        response = self.client.post(self.favourites_url, data=form_data)
        favourite = Substitute.objects.all()[1]
        
        self.assertEqual(favourite.initial_product_id, self.created_product_pk1)

class DeleteSubstitutesViewTest(BaseTest):
    
    def test_saved_substitutes_delete_favourite_success(self):
        self.client.force_login(self.user)
        response = self.client.post(self.delete_favourites_url, { 'substituteId': self.substitute.pk }, content_type='application/json')
        self.assertEqual(response.status_code, 204)
        
    def test_saved_substitutes_delete_favourite_bad_id(self):
        self.client.force_login(self.user)
        response = self.client.post(self.delete_favourites_url, { 'substituteId': 338 }, content_type='application/json')
        self.assertEqual(response.status_code, 404)
