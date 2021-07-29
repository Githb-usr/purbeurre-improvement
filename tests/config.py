#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Config file for tests
"""

from food.models import Product
from users.models import User, Substitute

# First test user account for Selenium
USER1_EMAIL = "test@tests.fr"
USER1_PASSWORD = "fhJGjgfjgfj45dshf"
USER1_USERNAME = "Toto38"
USER1_FIRSTNAME = "Robert"
USER1_LASTNAME = "Martin"

# Second test user account for Selenium
USER2_EMAIL = "usertest@tests.fr"
USER2_PASSWORD = "fhJGjgf1dfhdfhdshf"
USER2_USERNAME = "Robert"
USER2_FIRSTNAME = "Simon"
USER2_LASTNAME = "Scott"

# Partial raw data from Open Food Facts API
OFF_API_RAW_DATA = [
        {
            "brands": "Cristaline",
            "categories": "Boissons,Eaux,Eaux de sources,Eaux minérales,Eaux minérales naturelles",
            "code": "3274080005003",
            "image_url": "https://images.openfoodfacts.org/images/products/327/408/000/5003/front_fr.626.400.jpg",
            "nutrient_levels": {
                "fat": "low",
                "salt": "low",
                "saturated-fat": "low",
                # "sugars": "low"
            },
            "nutriments": {
                "fat": 0,
                "salt": 0,
                "saturated-fat": 0,
                "sugars": 0,
            },
            "nutriscore_grade": "a",
            "product_name": "Cristaline",
            "stores": "Carrefour,Leclerc,Auchan",
            "url": "https://fr.openfoodfacts.org/produit/3274080005003/cristaline-eau-de-source"
        },
        {
            "brands": "Ferrero",
            "categories": "Produits à tartiner sucrés, Pâtes à tartiner, Pâtes à tartiner aux noisettes, Pâtes à tartiner au chocolat, Pâtes à tartiner aux noisettes et au cacao",
            "code": "3017620422003",
            "image_url": "https://images.openfoodfacts.org/images/products/301/762/042/2003/front_fr.270.400.jpg",
            "nutrient_levels": {
                "fat": "high",
                "salt": "low",
                "saturated-fat": "high",
                "sugars": "high"
            },
            "nutriments": {
                "fat": 30.9,
                "salt": 0.107,
                "saturated-fat": 10.6,
                "sugars": 56.3,
            },
            "nutriscore_grade": "e",
            "product_name": "Nutella pate a tartiner noisettes-cacao",
            "stores": "Bi1,Magasins U,Carrefour,Franprix,Auchan",
            "url": "https://fr.openfoodfacts.org/produit/3017620422003/nutella-pate-a-tartiner-noisettes-cacao-t-400-pot-de-400-gr-ferrero"
        },
        {
            "brands": "Lu",
            "categories": "Snacks, Snacks sucrés, Biscuits et gâteaux, Biscuits, Biscuits au chocolat",
            "code": "7622210449283",
            "image_url": "https://images.openfoodfacts.org/images/products/762/221/044/9283/front_fr.429.400.jpg",
            "nutrient_levels": {
                "fat": "moderate",
                "salt": "moderate",
                "saturated-fat": "high",
                "sugars": "high"
            },
            "nutriments": {
                "fat": 17,
                "salt": 0.58,
                "saturated-fat": 5.6,
                "sugars": 32,
            },
            "nutriscore_grade": "d",
            "product_name": "Prince Chocolat",
            "stores": "Carrefour Market,Magasins U,Auchan,Intermarché,Carrefour,Casino,Leclerc,Cora,Bi1",
            "url": "https://fr.openfoodfacts.org/produit/7622210449283/prince-chocolat-lu"
        },
        {
            "brands": "Cocacola",
            "categories": "Beverages,Carbonated drinks,Artificially sweetened beverages,Sodas,Diet beverages,Non-Alcoholic beverages,Colas,Diet sodas,Diet cola soft drink",
            "code": "5449000131805",
            "nutrient_levels": {
                "fat": "low",
                "salt": "low",
                "saturated-fat": "low",
                "sugars": "low"
            },
            "nutriscore_grade": "c",
            "product_name": "Cocacola Zero",
            "url": "https://fr.openfoodfacts.org/produit/5449000131805/coca-cola-sans-sucres-cocacola"
        }
]

# The last product (Cocacola zero) is removed from the list because the "Stores" key is missing
PRODUCT_DICT_LIST = [
    {
            "brands": "Cristaline",
            "categories": "Boissons,Eaux,Eaux de sources,Eaux minérales,Eaux minérales naturelles",
            "code": "3274080005003",
            "image_url": "https://images.openfoodfacts.org/images/products/327/408/000/5003/front_fr.626.400.jpg",
            "nutrient_levels": {
                "fat": "low",
                "salt": "low",
                "saturated-fat": "low",
                # "sugars": "low"
            },
            "nutriments": {
                "fat": 0,
                "salt": 0,
                "saturated-fat": 0,
                "sugars": 0,
            },
            "nutriscore_grade": "a",
            "product_name": "Cristaline",
            "stores": "Carrefour,Leclerc,Auchan",
            "url": "https://fr.openfoodfacts.org/produit/3274080005003/cristaline-eau-de-source"
        },
        {
            "brands": "Ferrero",
            "categories": "Produits à tartiner sucrés, Pâtes à tartiner, Pâtes à tartiner aux noisettes, Pâtes à tartiner au chocolat, Pâtes à tartiner aux noisettes et au cacao",
            "code": "3017620422003",
            "image_url": "https://images.openfoodfacts.org/images/products/301/762/042/2003/front_fr.270.400.jpg",
            "nutrient_levels": {
                "fat": "high",
                "salt": "low",
                "saturated-fat": "high",
                "sugars": "high"
            },
            "nutriments": {
                "fat": 30.9,
                "salt": 0.107,
                "saturated-fat": 10.6,
                "sugars": 56.3,
            },
            "nutriscore_grade": "e",
            "product_name": "Nutella pate a tartiner noisettes-cacao",
            "stores": "Bi1,Magasins U,Carrefour,Franprix,Auchan",
            "url": "https://fr.openfoodfacts.org/produit/3017620422003/nutella-pate-a-tartiner-noisettes-cacao-t-400-pot-de-400-gr-ferrero"
        },
        {
            "brands": "Lu",
            "categories": "Snacks, Snacks sucrés, Biscuits et gâteaux, Biscuits, Biscuits au chocolat",
            "code": "7622210449283",
            "image_url": "https://images.openfoodfacts.org/images/products/762/221/044/9283/front_fr.429.400.jpg",
            "nutrient_levels": {
                "fat": "moderate",
                "salt": "moderate",
                "saturated-fat": "high",
                "sugars": "high"
            },
            "nutriments": {
                "fat": 17,
                "salt": 0.58,
                "saturated-fat": 5.6,
                "sugars": 32,
            },
            "nutriscore_grade": "d",
            "product_name": "Prince Chocolat",
            "stores": "Carrefour Market,Magasins U,Auchan,Intermarché,Carrefour,Casino,Leclerc,Cora,Bi1",
            "url": "https://fr.openfoodfacts.org/produit/7622210449283/prince-chocolat-lu"
        }
]

# Lists initially stored as strings. The data is now separated
SEPARATED_DATA = {
            'clean_brands': ['Cristaline', 'Ferrero', 'Lu'],
            'clean_categories': ['Boissons', 'Eaux', 'Eaux de sources', 'Eaux minérales', 'Eaux minérales naturelles', 'Produits à tartiner sucrés',\
                'Pâtes à tartiner', 'Pâtes à tartiner aux noisettes', 'Pâtes à tartiner au chocolat', 'Pâtes à tartiner aux noisettes et au cacao',\
                'Snacks', 'Snacks sucrés', 'Biscuits et gâteaux', 'Biscuits', 'Biscuits au chocolat'],
            'clean_stores': ['Magasins U', 'Carrefour Market', 'Franprix', 'Auchan', 'Intermarché', 'Carrefour', 'Leclerc', 'Bi1'],
            'brand_of_products': [
                ('3274080005003', 'Cristaline'),
                ('3017620422003', 'Ferrero'),
                ('7622210449283', 'Lu')
            ],
            'categories_of_products': [
                ('3274080005003', ['Boissons', 'Eaux', 'Eaux de sources', 'Eaux minérales', 'Eaux minérales naturelles']),
                ('3017620422003', ['Produits à tartiner sucrés', 'Pâtes à tartiner', 'Pâtes à tartiner aux noisettes', 'Pâtes à tartiner au chocolat', 'Pâtes à tartiner aux noisettes et au cacao']),
                ('7622210449283', ['Snacks', 'Snacks sucrés', 'Biscuits et gâteaux', 'Biscuits', 'Biscuits au chocolat'])],
            'stores_of_products': [
                ('3274080005003', ['Carrefour', 'Leclerc', 'Auchan']),
                ('3017620422003', ['Bi1', 'Magasins U', 'Carrefour', 'Franprix', 'Auchan']),
                ('7622210449283', ['Carrefour Market', 'Magasins U', 'Auchan', 'Intermarché', 'Carrefour'])
            ],
        }

BRANDS_FIELD_STRING = 'Cristaline,Nutella,Haribo'
CLEAN_BRANDS_FIELD_LIST = 'Cristaline'

CATEGORIES_FIELD_STRING = 'Snacks, Snacks sucrés, Biscuits et gâteaux, Biscuits, Biscuits au chocolat'
CLEAN_CATEGORIES_FIELD_LIST = ['Snacks', 'Snacks Sucrés', 'Biscuits Et Gâteaux', 'Biscuits', 'Biscuits Au Chocolat']

STORES_FIELD_STRING = 'Bi1,Magasins U,Carrefour,Franprix,Auchan'
CLEAN_STORES_FIELD_LIST = ['Bi1', 'Magasins U', 'Carrefour', 'Franprix', 'Auchan']
