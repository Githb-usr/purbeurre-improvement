#!/usr/bin/env python
# -*- coding: utf-8 -*-

from food.data_cleaner import DataCleaner
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
        self.data_cleaner = DataCleaner()
        self.raw_data = []
        self.products_dict_list = []
        self.clean_product_fields = {}

    def get_api_data(self):
        """
            xxx
            :param field_string: xxx
            :return: xxxx
            :rtype: xxx
        """
        self.raw_data = self.off_api.get_full_api_products()
        self.products_dict_list = self.data_cleaner.create_products_dict_list(self.raw_data)
        self.clean_product_fields = self.data_cleaner.extract_strings_field(self.products_dict_list)

    def populate_database_with_products(self):
        """
            xxx
            :param field_string: xxx
            :return: xxxx
            :rtype: dict()
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
                            novascore = prod_dict['nova_group'],
                            url = prod_dict['url']
                        )
                        product.save()
                        all_products = Product.objects.all().order_by('-id')

        return all_products

    def populate_database_with_categories(self):
        """
            xxx
            :param field_string: xxx
            :return: xxxx
            :rtype: dict()
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
                all_categories = Category.objects.all().order_by('-id')
                
        return all_categories
    
    def populate_database_with_category_products(self):
        """
            xxx
            :param field_string: xxx
            :return: xxxx
            :rtype: dict()
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
            xxx
            :param field_string: xxx
            :return: xxxx
            :rtype: dict()
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
                all_stores = Store.objects.all().order_by('-id')

        return all_stores

    def populate_database_with_store_products(self):
        """
            xxx
            :param field_string: xxx
            :return: xxxx
            :rtype: dict()
        """
        # Save the store_product in database
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
