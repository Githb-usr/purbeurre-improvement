#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import get_user_model
from django.conf import settings
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys

from tests.functionnal.config import USER_EMAIL, USER_PASSWORD, USER_USERNAME, USER_FIRSTNAME, USER_LASTNAME

firefox_options = webdriver.FirefoxOptions()
firefox_options.headless = True

class FirefoxFunctionalTestCases(StaticLiveServerTestCase):
    """
       This class allows us to test the different search engines of the application for Firefox browser
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = webdriver.Firefox(
            executable_path=str(settings.BASE_DIR / 'webdrivers' / 'geckodriver'),
            options=firefox_options,
        )
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.driver.quit()

    def setUp(self):
        User = get_user_model()
        User.objects.create_user(            
            username=USER_USERNAME,
            first_name=USER_FIRSTNAME,
            last_name=USER_LASTNAME,
            email=USER_EMAIL,
            password=USER_PASSWORD,
        )

    def test_login_form(self):
        """
            We test the login form
        """
        # We call the web application
        self.driver.get(self.live_server_url)
        # We go to the login page
        self.driver.find_element_by_class_name('connect-link').click()
        # We localise the text field and we enter and confirm a email
        login_email = self.driver.find_element_by_id("id_username").send_keys(USER_EMAIL)
        # idem for password
        login_password = self.driver.find_element_by_id("id_password").send_keys(USER_PASSWORD)
        # We submit form
        self.driver.find_element_by_css_selector("section.main-section form button").click()
        
        logout = self.driver.find_element_by_xpath("//i[@title='Déconnexion']")
        
        self.assertEqual(
            logout.text,
            "Déconnexion",
            "Disconnect button should be available.",
        )

        self.driver.close()
        
    def test_registration_form(self):
        """
            We delete the test account so we can run a new test
        """
        # We create a Firefox session
        # driver = webdriver.Firefox()
        # driver.implicitly_wait(30)
        # driver.maximize_window()

        # We call the web application
        self.driver.get(self.live_server_url)
        # We go to the registration page
        self.driver.find_element_by_class_name('register-link').click()

        # We localise the text field and we enter and confirm a email
        register_email = self.driver.find_element_by_id("id_email").send_keys(USER_EMAIL)

        # Idem for firstname, lastname and username
        register_email = self.driver.find_element_by_id("id_first_name").send_keys(USER_FIRSTNAME)        
        register_email = self.driver.find_element_by_id("id_last_name").send_keys(USER_LASTNAME)
        register_email = self.driver.find_element_by_id("id_username").send_keys(USER_USERNAME)
        
        # Idem for password (x2)
        register_password1 = self.driver.find_element_by_id("id_password1").send_keys(USER_PASSWORD)
        register_password2 = self.driver.find_element_by_id("id_password2").send_keys(USER_PASSWORD)
        
        self.driver.find_element_by_css_selector("section.main-section form button").click();

        # We close the browser window
        self.driver.close()

    def test_homepage_large_search_form(self):
        """
          We test the large search engine on the homepage
        """
        self.base_test_function('', 'large-search-form')
        
    def test_homepage_small_search_form(self):
        """
          We test the small search engine on the homepage
        """
        self.base_test_function('', 'small-search-form')
        
    def test_another_page_small_search_form(self):
        """
          We test the small search engine on another page (the legal notices page)
        """
        self.base_test_function('legal_notices/', 'small-search-form')
        
    def base_test_function(self, url_fragment, element_id):
        # We create a Firefox session
        # driver = webdriver.Firefox()
        # driver.implicitly_wait(15)
        # driver.maximize_window()

        # We call the web application
        self.driver.get(self.live_server_url + url_fragment)

        # We localise the text field 
        search_field = self.driver.find_element_by_id(element_id)
        search_field.clear()

        # We enter and confirm a search keyword
        search_field.send_keys("nutella")
        search_field.submit()

        # We look at the list of results displayed after the search
        # using the find_elements_by_class_name method
        lists= self.driver.find_elements_by_class_name("product-card")

        # We review the elements and return the individual content
        i = 0
        for listitem in lists:
          print (listitem.get_attribute("innerHTML"))
          i += 1
          if(i > 2):
            break

        # We close the browser window
        self.driver.close()