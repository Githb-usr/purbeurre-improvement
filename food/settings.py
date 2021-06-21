#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Settings file
    To manage application constants
"""

# Basic url for connecting to the Open Food Facts API
API_BASE_URL = "https://fr.openfoodfacts.org/cgi/search.pl"

#Number of products to be downloaded each time you connect to the API
PAGE_SIZE = 500

# Number of connections to the API
PAGE_NUMBER = 3

# Fields of products to keep and download (It's a parameter of the connection to the API)
FIELDS_OF_PRODUCT = 'code,product_name,brands,categories,nutriscore_grade,nutriments,nutrient_levels,stores,url,image_url'

# List of product fields to keep and download
FIELDS_OF_PRODUCT_LIST = ('code', 'product_name', 'brands', 'categories', 'nutriscore_grade', 'stores', 'url', 'image_url')

# Only the categories with a number of products between these 2 numbers are recovered.
MINIMUM_NUMBER_OF_PRODUCTS_PER_CATEGORY = 25
MAXIMUM_NUMBER_OF_PRODUCTS_PER_CATEGORY = 75

NO_DATA = "no_data"

STOPWORDS = ["-","a","ah","ai","aie","ait","as","au","aux","b","bah","bas","bat","bot","c","c'est","car","ce","ces","ci","d","da","de","des","du","dès","e","eh","en","es","est","et","etc","etre","eu","euh","eux","f","fi","g","h","ha","hem","hi","ho","hé","i","il","ils","j","je","k","l","la","las","le","les","lui","là","lès","m","ma","me","n","na","ne","ni","non","nos","nt","nul","o","oh","olé","on","ont","ou","o|","où","p","paf","par","pas","peu","pu","q","qu","que","r","s","sa","se","ses","si","son","sur","t","ta","tac","te","tes","toi","ton","tu","té","u","un","une","unes","uns","v","va","vais","vas","vers","via","vos","vu","vé","w","x","y","z","zut","à","â","ça","ès","été","ô"]
