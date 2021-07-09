#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from config.settings import BASE_DIR
from food.api_data_cleaner import ApiDataCleaner
from food.models import Product, Category, Store
from food.off_api import OffApi

class DatabaseService:
    """
        DatabaseService class
        To manage the population of the database
    """

    def __init__(self):
        """ Constructor """
        self.off_api = OffApi()
        self.data_cleaner = ApiDataCleaner()
        self.raw_data = []
        self.products_dict_list = []
        self.clean_product_fields = {}

    def get_api_data(self):
        """
            We get the data from the API and then clean it up
        """
        self.raw_data = self.off_api.get_full_api_products()
        self.products_dict_list = self.data_cleaner.create_products_dict_list(self.raw_data)
        self.clean_product_fields = self.data_cleaner.extract_strings_field(self.products_dict_list)

    def populate_database_with_products(self):
        """
            We populate the "food_product" table of the database
        """
        all_products = {}
        # Save the products in database
        for prod_dict in self.products_dict_list:
            for brand in self.clean_product_fields['brand_of_products']:
                if brand[0] == prod_dict['code']:
                    product_to_create = Product.objects.filter(barcode=prod_dict['code']).exists()
                    if product_to_create == False:
                        product = Product(
                            designation = prod_dict['product_name'],
                            brand = brand[1],
                            barcode = prod_dict['code'],
                            nutriscore = prod_dict['nutriscore_grade'].capitalize(),
                            fat_value = self.get_field_value(prod_dict, 'fat'),
                            fat_level = self.transcribe_nutrient_level(prod_dict, 'fat'),
                            saturated_fat_value = self.get_field_value(prod_dict, 'saturated-fat'),
                            saturated_fat_level = self.transcribe_nutrient_level(prod_dict, 'saturated-fat'),
                            sugars_value = self.get_field_value(prod_dict, 'sugars'),
                            sugars_level = self.transcribe_nutrient_level(prod_dict, 'sugars'),
                            salt_value = self.get_field_value(prod_dict, 'salt'),
                            salt_level = self.transcribe_nutrient_level(prod_dict, 'salt'),
                            url = prod_dict['url'],
                            image_url = self.get_image_url(prod_dict, 'image_url')
                        )
                        product.save()

    def get_field_value(self, prod_dict, field):
        """
            We recover the amount of each nutrient in a product
            :param prod_dict: Dictionary containing all the data of a product
            :param field: the name of nutrient (in Open Food Fact database)
            :return: quantity of nutrient for 100g
            :rtype: float
        """
        try:
            if prod_dict['nutriments'][field]:
                return prod_dict['nutriments'][field]
            # No value = 0g of nutrient
            return 0
        # No key = nutrient missing from the product
        except KeyError:
                return None

    def get_image_url(self, prod_dict, url_field_name):
        """
            We get the URL of the product to display its picture
            :param prod_dict: Dictionary containing all the data of a product
            :param url_field_name: the name of picture URL field (in Open Food Fact database)
            :return: an URL
            :rtype: string
        """
        try:
            if prod_dict[url_field_name]:
                return prod_dict[url_field_name]
        # If there is no image, we put a default image
        except KeyError:
            return os.path.join(BASE_DIR, 'static/dist/assets/img/default_product_img.png')

    def transcribe_nutrient_level(self, prod_dict, nutriment):
        """
            The nutrient level is offered a full word. We store it as a 2-letter abbreviation.
            :param prod_dict: Dictionary containing all the data of a product
            :param nutriment: the name of nutrient (in Open Food Fact database)
            :return: the nutrient level
            :rtype: string
        """
        try:
            level = prod_dict['nutrient_levels'][nutriment]
            if level == 'low':
                return 'LO'
            elif level == 'moderate':
                return 'MO'
            elif level == 'high':
                return 'HI'
        except KeyError:
            return None

    def populate_database_with_categories(self):
        """
            We populate the "food_category" table of the database
        """
        all_categories = {}
        # Save the categories in database
        for clean_cat in self.clean_product_fields['clean_categories']:
            category_to_create = Category.objects.filter(designation=clean_cat).exists()
            if category_to_create == False:
                category = Category(
                    designation = clean_cat
                )
                category.save()

    def populate_database_with_category_products(self):
        """
            We populate the "category_products" table of the database
        """
        # Create the product_category objects
        # For 1 tuple 'product barcode/category list'
        for category_prod in self.clean_product_fields['categories_of_products']:
            # For 1 category of category list
            for category in category_prod[1]:
                # For 1 category of the database
                for category_objet in Category.objects.all():
                    # If the category of category list == the name of the database category
                    if category == category_objet.designation:
                        # If product and category are in database
                        category_to_link = Category.objects.filter(designation=category).exists()
                        product_to_link = Product.objects.filter(barcode=category_prod[0]).exists()
                        if category_to_link == True and product_to_link == True:
                            # We save product id and category id in the category_products table
                            category_objet.products.add(Product.objects.get(barcode=category_prod[0]))

    def populate_database_with_stores(self):
        """
            We populate the "food_store" table of the database
        """
        all_stores = {}
        # Save the stores in database
        for clean_sto in self.clean_product_fields['clean_stores']:
            store_to_create = Store.objects.filter(designation=clean_sto).exists()
            if store_to_create == False:
                store = Store(
                    designation = clean_sto
                )
                store.save()

    def populate_database_with_store_products(self):
        """
            We populate the "store_products" table of the database
        """
        # For 1 tuple 'product barcode/store list'
        for store_prod in self.clean_product_fields['stores_of_products']:
            # For 1 store of store list
            for store in store_prod[1]:
                # For 1 store of the database
                for store_objet in Store.objects.all():
                    # If the store of store list == the name of the database store
                    if store == store_objet.designation:
                        # If product and store are in database
                        store_to_link = Store.objects.filter(designation=store).exists()
                        product_to_link = Product.objects.filter(barcode=store_prod[0]).exists()
                        if store_to_link == True and product_to_link == True:
                            # We save product id and store id in the store_products table
                            store_objet.products.add(Product.objects.get(barcode=store_prod[0]))
