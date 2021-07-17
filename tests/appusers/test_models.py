#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model
from django.test import Client, TestCase

from food.models import Product
from users.models import UserManager, User, Substitute

class BaseTest(TestCase):
    def setUp(self):
        # Set up non-modified objects used by all test methods
        User = get_user_model()
        self.user_id = User.objects.create_user(
            username='Hopopop',
            first_name='Nicolas',
            last_name='Martin',
            email='nicolas.martin@free.fr',
            ).pk

        self.prod_id = Product.objects.create(
            designation='Nesquik',
            barcode='3033710065967',
            brand='Nestlé',
            nutriscore='B',
            fat_value='3',
            fat_level='MO',
            saturated_fat_value='1.5',
            saturated_fat_level='MO',
            sugars_value='75',
            sugars_level='HI',
            salt_value='0.4',
            salt_level='MO',
            url='https://fr.openfoodfacts.org/produit/3033710065967/nesquik-nestle',
            image_url='https://static.openfoodfacts.org/images/products/303/371/006/5967/front_fr.266.400.jpg'
            ).pk

        self.sub_prod_id = Product.objects.create(
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

        self.sub_id = Substitute.objects.create(
            creation_date='2021-07-10 17:44:36.156367+02',
            initial_product_id=self.prod_id,
            substituted_product_id=self.sub_prod_id,
            ).pk

        return super().setUp()
    
class UserManagerTestCase(BaseTest):
    def test_create_user_with_invalid_mail(self):
        with self.assertRaises(ValueError) as cm:
            get_user_model().objects.create_user(email='', username='testuser', first_name='Laurent', last_name='Dupond')
        email_error = cm.exception
        self.assertEqual(str(email_error), 'Vous devez entrer un email valide')
        
    def test_create_user_ok(self):
        user = get_user_model().objects.create_user(
            username='testuser2',
            first_name='Laurent',
            last_name='Dupond',
            email='hip@test.com',
            password='fhh456GG455t'
            )
        self.assertEqual(user.email, 'hip@test.com')
        self.assertTrue(user.check_password('fhh456GG455t'))

class UserModelTestCase(BaseTest):

    def test_username_label(self):
        user = User.objects.get(id=self.user_id)
        field_label = user._meta.get_field('username').verbose_name
        self.assertEquals(field_label, 'Pseudonyme')

    def test_first_name_label(self):
        user = User.objects.get(id=self.user_id)
        field_label = user._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'Prénom')

    def test_last_name_label(self):
        user = User.objects.get(id=self.user_id)
        field_label = user._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'Nom')

    def test_email_label(self):
        user = User.objects.get(id=self.user_id)
        field_label = user._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'Adresse email')

    def test_avatar_label(self):
        user = User.objects.get(id=self.user_id)
        field_label = user._meta.get_field('avatar').verbose_name
        self.assertEquals(field_label, 'avatar')

    def test_updated_at_label(self):
        user = User.objects.get(id=self.user_id)
        field_label = user._meta.get_field('updated_at').verbose_name
        self.assertEquals(field_label, 'Dernière modification')

    def test_is_active_label(self):
        user = User.objects.get(id=self.user_id)
        field_label = user._meta.get_field('is_active').verbose_name
        self.assertEquals(field_label, 'is active')

    def test_is_admin_label(self):
        user = User.objects.get(id=self.user_id)
        field_label = user._meta.get_field('is_admin').verbose_name
        self.assertEquals(field_label, 'is admin')

    def test_username_max_length(self):
        user = User.objects.get(id=self.user_id)
        max_length = user._meta.get_field('username').max_length
        self.assertEquals(max_length, 30)

    def test_first_name_max_length(self):
        user = User.objects.get(id=self.user_id)
        max_length = user._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 30)
        
    def test_last_name_max_length(self):
        user = User.objects.get(id=self.user_id)
        max_length = user._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 30)
        
    def test_email_max_length(self):
        user = User.objects.get(id=self.user_id)
        max_length = user._meta.get_field('email').max_length
        self.assertEquals(max_length, 255)

    def test_object_name_is_username(self):
        user = User.objects.get(id=self.user_id)
        expected_object_name = user.username
        self.assertEquals(expected_object_name, str(user))

    def test_get_full_name(self):
        user = User.objects.get(id=self.user_id)
        expected_full_name = f'{user.first_name} {user.last_name}'
        self.assertEquals(expected_full_name, user.get_full_name())

class SubstituteModelTestCase(BaseTest):

    def test_creation_date_label(self):
        substitute = Substitute.objects.get(id=self.sub_id)
        field_label = substitute._meta.get_field('creation_date').verbose_name
        self.assertEquals(field_label, 'creation date')