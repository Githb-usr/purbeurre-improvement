#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import OrderedDict
import re
import unicodedata

from food.settings import NO_DATA

class Parser:
    """
        Parser class
        To manage user question parsing
    """
    def __init__(self):
        """ Constructor """
        self.cleaned_string = ''
        self.cleaned_string_words_list = []

    def refuse_empty_string(self, raw_string):
        """
            We check that the user input value is not empty or made up of spaces
            :param: raw_string is a string
            :return: a string "no_data" indicating that the response is empty
            or consists of spaces
            :rtype: string
        """
        trim_raw_string = raw_string.strip()
        if re.match(r"^(?![\s\S])", trim_raw_string):
            return NO_DATA

    def remove_accented_characters(self, raw_string):
        """
            String cleaning to facilitate comparisons, step 1
            :param: raw_string is a string
            :return: a string without accented characters and in lower case
            :rtype: string
            Example : "Pâte à tartiner" --> "pate a tartiner"
        """
        trimmed_string = raw_string.strip()
        # We replace the accented characters and use lower case
        no_accent_data = ''.join(
            (c for c in unicodedata.normalize('NFD', trimmed_string)
             if unicodedata.category(c) != 'Mn')
            )

        return no_accent_data.lower()

    def remove_special_characters(self, raw_string):
        """
            String cleaning to facilitate comparisons, step 2
            :param: raw_string is a string
            :return: a string without special characters
            :rtype: string
            Example : "l'horloge de# no$tre-dame tourne ?" --> "l'horloge de notre-dame tourne"
        """
        # We delete the letters with quote (l', d', etc.)
        no_quote_letter_data = re.sub(r"(\s[a-z])'", " ", raw_string)
        # We delete the special characters except the hyphen
        return re.sub(r'[^\-\'\,\w\s]','',no_quote_letter_data)

    def get_cleaned_string(self, raw_string):
        """
            Reconstruction of a string from the list of important words
            :param: raw_string is a raw string to parse
            :return: a parsed/cleaned string without accents, special
            charatcters or unnecessary words
            :rtype: string
        """
        if self.refuse_empty_string(raw_string) == NO_DATA:
            print("La question de l'utilisateur est vide ou constituée d'espaces.")
            return NO_DATA

        # We remove any accents and special characters (punctuation and others)
        no_accent_data = self.remove_accented_characters(raw_string)

        return self.remove_special_characters(no_accent_data)
