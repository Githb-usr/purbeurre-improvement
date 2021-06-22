#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import template

register = template.Library()

@register.filter 
def get_dict_value(dictionary, key): 
    return dictionary.get(key)