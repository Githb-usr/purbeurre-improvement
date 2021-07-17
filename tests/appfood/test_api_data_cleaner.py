#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.test import SimpleTestCase, TestCase

from food.api_data_cleaner import ApiDataCleaner
import tests.config as test_result

class BaseTest(SimpleTestCase):
    def setUp(self):
        self.api_data_cleaner = ApiDataCleaner()

        return super().setUp()

class ApiDataCleanerTestCase(BaseTest):

    def test_create_products_dict_list(self):
        # We remove products for which information is missing
        products_dict_list = self.api_data_cleaner.create_products_dict_list(test_result.OFF_API_RAW_DATA)
        self.assertEqual(products_dict_list, test_result.PRODUCT_DICT_LIST)

    def test_extract_strings_field(self):
        # We extract the information stored as strings that we need separately
        separated_data = self.api_data_cleaner.extract_strings_field(test_result.PRODUCT_DICT_LIST)
        self.assertCountEqual(separated_data['clean_brands'], test_result.SEPARATED_DATA['clean_brands'])
        self.assertCountEqual(separated_data['clean_categories'], test_result.SEPARATED_DATA['clean_categories'])
        self.assertCountEqual(separated_data['clean_stores'], test_result.SEPARATED_DATA['clean_stores'])
        self.assertCountEqual(separated_data['brand_of_products'], test_result.SEPARATED_DATA['brand_of_products'])
        self.assertCountEqual(separated_data['categories_of_products'], test_result.SEPARATED_DATA['categories_of_products'])
        self.assertCountEqual(separated_data['stores_of_products'], test_result.SEPARATED_DATA['stores_of_products'])

    def test_clean_fields(self):
        clean_categories_field_list = self.api_data_cleaner.clean_proper_names_fields(test_result.CATEGORIES_FIELD_STRING)
        self.assertEqual(clean_categories_field_list, test_result.CLEAN_CATEGORIES_FIELD_LIST)
    
    def test_clean_proper_names_fields(self):
        clean_stores_field_list = self.api_data_cleaner.clean_proper_names_fields(test_result.STORES_FIELD_STRING)
        self.assertEqual(clean_stores_field_list, test_result.CLEAN_STORES_FIELD_LIST)
        
    def test_clean_brands_field(self):
        clean_brand_field_list = self.api_data_cleaner.clean_brands_field(test_result.BRANDS_FIELD_STRING)
        self.assertEqual(clean_brand_field_list, test_result.CLEAN_BRANDS_FIELD_LIST)
