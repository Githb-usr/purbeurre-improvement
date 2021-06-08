#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import time

from food.setting import API_BASE_URL, PAGE_SIZE, PAGE_NUMBER, FIELDS_OF_PRODUCT

class OffApi:
    """
        OffApi class
        To manage Open Food Facts API data recovery
    """

    def get_api_products(self, page_number):
        """
            We retrieve the raw data (products) from the api
            :return: json data
            :rtype: list()
        """
        params = {
            'action': 'process',
            'json': 'true', # Get JSON data
            'page_size': PAGE_SIZE, # Number of products per page downloaded
            'page': page_number, # Number of product pages you want to download
            'fields': FIELDS_OF_PRODUCT, # List of fields to keep among all the existing ones
            'sort_by': 'unique_scans_n' # Sorting by most popular products
            }
        headers = {'User-Agent': 'NameOfYourApp - Android - Version 1.0 - www.yourappwebsite.com'}
        result = requests.get(API_BASE_URL, headers = headers, params = params)
        if result.status_code == 200:
            data = result.json()
            products_data = data['products'] # Only the value of the 'products' key is kept (there are other keys in the JSON object).
            
            return products_data
        else:
            print("La connexion à l'API d'Open Food Facts a échoué.")
            print("Nouvelle tentative.")
            self.get_full_api_products()

    def get_full_api_products(self):
        """
            We recover as many pages of raw data as defined in the application configuration
            (see settings file).
            :return: json data
            :rtype: list()
        """
        full_products_data = []

        for i in range(1, PAGE_NUMBER + 1):
            products_data = self.get_api_products(i)
            for data in products_data:
                full_products_data.append(data)
                
            time.sleep(1)

        return full_products_data
