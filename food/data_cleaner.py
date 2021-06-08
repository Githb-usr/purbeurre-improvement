#!/usr/bin/env python
# -*- coding: utf-8 -*-

from food.off_api import OffApi

from food.setting import FIELDS_OF_PRODUCT_LIST

class DataCleaner:
    """
        DataCleaner class
        To manage data cleaning from the Open Food Facts API
    """

    def __init__(self):
        """ Constructor """
        self.products_dict_list = []
        # self.clean_brands = []
        # self.clean_categories = []
        # self.clean_stores = []
        # self.brand_of_products = []
        # self.cats_of_products = []
        # self.stores_of_products = []

    def create_products_dict_list(self, raw_data):
        """
            Products are retrieved via the Open Food Facts API,
            but only those with all the required fields.
            :return: A list of dictionaries is obtained, one dictionary per product.
            :rtype: list()
        """
        complete_data = []
        # Deletion of products with empty fields
        complete_data = [
                product for product in raw_data
                if len(product) == len(FIELDS_OF_PRODUCT_LIST) and all(product.values())            
            ]

        # Creation of the dictionary containing all the complete products
        for data in complete_data:
            self.products_dict_list.append(data)

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
            clean_brands = list(set(clean_brands))

            # For the 'categories' field
            product_clean_categories = self.clean_fields(product['categories'])
            categories_of_products.append((product['code'], product_clean_categories))
            for category in product_clean_categories:
                if category != '':
                    clean_categories.append(category)
            clean_categories = list(set(clean_categories))

            # For the 'stores' field
            product_clean_stores = self.clean_fields(product['stores'])
            stores_of_products.append((product['code'], product_clean_stores))
            for store in product_clean_stores:
                if store != '':
                    clean_stores.append(store)
            clean_stores = list(set(clean_stores))

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
            are transformed into a list
            after standardization of the spaces.
            :param field_string: string with several values separated by commas
            :return: A list of values is obtained instead of a string
            :rtype: list()
        """
        clean_field_list = []

        field_split = field_string.split(',')
        for value in field_split:
            value_strip = value.strip().capitalize()
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
        clean_field_list = self.clean_fields(field_string)

        return clean_field_list[0].title()
