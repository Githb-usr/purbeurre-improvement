#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

class TestSearchForm:
    """
       This class allows us to test the different search engines of the application for Chrome browser
    """
    # def test_homepage_large_search_form(self):
    #     """
    #       We test the large search engine on the homepage
    #     """
    #     self.base_test_function('', 'large-search-form')
        
    # def test_homepage_small_search_form(self):
    #     """
    #       We test the small search engine on the homepage
    #     """
    #     self.base_test_function('', 'small-search-form')
        
    # def test_another_page_small_search_form(self):
    #     """
    #       We test the small search engine on another page (the legal notices page)
    #     """
    #     self.base_test_function('legal_notices/', 'small-search-form')
        
    # def base_test_function(self, url_fragment, element_id):
    #     # We create a Firefox session
    #     driver = webdriver.Chrome()
    #     driver.implicitly_wait(30)
    #     driver.maximize_window()

    #     # We call the web application
    #     driver.get(BASE_URL + url_fragment)

    #     # We localise the text field 
    #     search_field = driver.find_element_by_id(element_id)
    #     search_field.clear()

    #     # We enter and confirm a search keyword
    #     search_field.send_keys("nutella")
    #     search_field.submit()

    #     # We look at the list of results displayed after the search
    #     # using the find_elements_by_class_name method
    #     lists= driver.find_elements_by_class_name("product-card")

    #     # We review the elements and return the individual content
    #     i = 0
    #     for listitem in lists:
    #       print (listitem.get_attribute("innerHTML"))
    #       i += 1
    #       if(i > 2):
    #         break

    #     # We close the browser window
    #     driver.close()