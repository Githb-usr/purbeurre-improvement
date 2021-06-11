#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Settings file
    To manage application constants
"""

# Basic url for connecting to the Open Food Facts API
API_BASE_URL = "https://fr.openfoodfacts.org/cgi/search.pl"

#Number of products to be downloaded each time you connect to the API
PAGE_SIZE = 10

# Number of connections to the API
PAGE_NUMBER = 1

# Fields of products to keep and download (It's a parameter of the connection to the API)
FIELDS_OF_PRODUCT = 'code,product_name,brands,categories,nutriscore_grade,nova_group,stores,url,image_url'

# List of product fields to keep and download
FIELDS_OF_PRODUCT_LIST = ('code', 'product_name', 'brands', 'categories', 'nutriscore_grade', 'nova_group', 'stores', 'url', 'image_url')

# Only the categories with a number of products between these 2 numbers are recovered.
MINIMUM_NUMBER_OF_PRODUCTS_PER_CATEGORY = 25
MAXIMUM_NUMBER_OF_PRODUCTS_PER_CATEGORY = 75

NO_DATA = "no_data"
