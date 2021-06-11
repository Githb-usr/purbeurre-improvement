#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError

from food.database_service import DatabaseService
from food.models import Product, Category, Store

class Command(BaseCommand):
    help = 'Extract data from the Open Food Fact API for populate the database'

    def handle(self, *args, **options):
        """
            xxx
            :param field_string: xxx
            :return: xxxx
            :rtype: xxx
        """
        database_service = DatabaseService()
        # Extract raw data from API
        database_service.get_api_data()
        # Populate product table
        database_service.populate_database_with_products()
        # Populate category table
        database_service.populate_database_with_categories()
        # Populate category-products table
        database_service.populate_database_with_category_products()
        # Populate store table
        database_service.populate_database_with_stores()
        # Populate store-products table
        database_service.populate_database_with_store_products()
