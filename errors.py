#!/usr/bin/env python
# -*- coding: utf-8 -*-

class OffBadRequestError(Exception):
    """
        To capture request errors when connecting to the OpenFoodFact API
    """

class OffJsonError(Exception):
    """
        To catch errors due to empty or incomplete JSON from the OpenFoodFact API
    """

class OffNetworkError(Exception):
    """
        To capture network errors from the OpenFoodFact API
    """
