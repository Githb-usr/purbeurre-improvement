#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import OrderedDict
import unicodedata

from food.off_api import OffApi
from food.settings import FIELDS_OF_PRODUCT_LIST

class ApiDataCleaner:
    """
        DataCleaner class
        To manage data cleaning from the Open Food Facts API
    """

    def __init__(self):
        """ Constructor """
        self.products_dict_list = []

    def create_products_dict_list(self, raw_data):
        """
            Products are retrieved via the Open Food Facts API,
            but only those with all the required fields.
            :return: A list of dictionaries is obtained, one dictionary per product.
            :rtype: list()
        """
        # Deletion of products with empty fields
        self.products_dict_list = [
        product for product in raw_data
        if len(product) == (len(FIELDS_OF_PRODUCT_LIST) + 2) and all(product.values())
        ]        

        return self.products_dict_list

    def extract_strings_field(self, products_dict_list):
        """ Retrieving multiple data contained in strings """
        brand_of_products = []
        categories_of_products = []
        stores_of_products = []
        clean_brands = []
        clean_categories = []
        clean_stores = []
        
        for product in products_dict_list:

            # For the 'brands' field
            product_clean_brand = self.clean_brands_field(product['brands'])
            brand_of_products.append((product['code'], product_clean_brand))
            if product_clean_brand != '':
                clean_brands.append(product_clean_brand)
            clean_brands = list(OrderedDict.fromkeys(clean_brands))

            # For the 'categories' field
            all_product_clean_categories = self.clean_fields(product['categories'])
            # We only keep the last 5 categories, the most specific to the product
            product_clean_categories = all_product_clean_categories[-5:]
            categories_of_products.append((product['code'], product_clean_categories))
            for category in product_clean_categories:
                if category != '':
                    clean_categories.append(category)
            clean_categories = list(OrderedDict.fromkeys(clean_categories))

            # For the 'stores' field
            product_clean_stores = self.clean_proper_names_fields(product['stores'])
            stores_of_products.append((product['code'], product_clean_stores))
            for store in product_clean_stores:
                if store != '':
                    clean_stores.append(store)
            clean_stores = list(OrderedDict.fromkeys(clean_stores))

        return {
            'clean_brands': clean_brands,
            'clean_categories': clean_categories,
            'clean_stores': clean_stores,
            'brand_of_products': brand_of_products,
            'categories_of_products': categories_of_products,
            'stores_of_products': stores_of_products
        }

    def clean_fields(self, field_string):
        """
            The strings of the products_dict_list containing several values
            are transformed into a list after standardization of the spaces.
            :param field_string: string with several values separated by commas
            :return: A list of values is obtained instead of a string
            :rtype: list()
        """
        clean_field_list = []
        field_split = field_string.split(',')
        for value in field_split:
            # We capitalize only the first word of the expression
            value_strip = value.strip().lower().capitalize()
            clean_field_list.append(value_strip)
        # We remove duplicates by keeping the order of the categories
        clean_field_list = list(OrderedDict.fromkeys(clean_field_list))

        return clean_field_list
    
    def clean_proper_names_fields(self, field_string):
        """
            The strings of the products_dict_list containing several values
            are transformed into a list after standardization of the spaces.
            :param field_string: string with several values separated by commas
            :return: A list of values is obtained instead of a string
            :rtype: list()
        """
        clean_field_list = []

        field_split = field_string.split(',')
        for value in field_split:
            # We capitalize each word of the expression
            value_strip = value.strip().lower().title()
            clean_field_list.append(value_strip)

        clean_field_list = list(set(clean_field_list))

        return clean_field_list
    
    def clean_brands_field(self, field_string):
        """
            Strings in the product brand field containing several values are transformed
            into strings containing a single value (the first one).
            :param field_string: string with several values separated by commas
            :return: A string with one brand only
            :rtype: string
        """
        clean_field_list = self.clean_proper_names_fields(field_string)

        return clean_field_list[0].title()
