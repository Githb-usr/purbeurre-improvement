#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models
from django.urls import reverse

class Product(models.Model):
    """
    Model of the "food_product" table in the database
    """
    designation = models.CharField(max_length=250)
    barcode = models.CharField(max_length=13)
    brand = models.CharField(max_length=60)
    nutriscore = models.CharField(max_length=1)
    
    # data for nutrient fields
    LOW_LEVEL = 'LO'
    MODERATE_LEVEL = 'MO'
    HIGH_LEVEL = 'HI'
    NUTRIENT_LEVELS = [
        (LOW_LEVEL, 'faible quantité'),
        (MODERATE_LEVEL, 'quantité modérée'),
        (HIGH_LEVEL, 'quantité élevée'),
    ]
    
    fat_value = models.FloatField(null=True)
    fat_level = models.CharField(
        max_length=2,
        choices=NUTRIENT_LEVELS,
        default=None,
        null=True
        )
    saturated_fat_value = models.FloatField(null=True)
    saturated_fat_level = models.CharField(
        max_length=2,
        choices=NUTRIENT_LEVELS,
        default=None,
        null=True
        )
    sugars_value = models.FloatField(null=True)
    sugars_level = models.CharField(
        max_length=2,
        choices=NUTRIENT_LEVELS,
        default=None,
        null=True
        )
    salt_value = models.FloatField(null=True)
    salt_level = models.CharField(
        max_length=2,
        choices=NUTRIENT_LEVELS,
        default=None,
        null=True
        )
    # URL of the product sheet on Open Food Facts website
    url = models.URLField(max_length=200)
    # URL of the product image on Open Food Facts website
    image_url = models.URLField(max_length=150)
    substitutes = models.ManyToManyField(
        'food.Product',
        through='users.Substitute',
        symmetrical = False
    )

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.designation

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('product_detail', args=[str(self.barcode)])

    class Meta:
        verbose_name_plural = "products"

class Category(models.Model):
    """
    Model of the "food_category" table in the database
    """
    designation = models.CharField(max_length=150, unique=True)
    products = models.ManyToManyField(Product, related_name='categories')

    def __str__(self):
        return self.designation

    class Meta:
        verbose_name_plural = "categories"

class Store(models.Model):
    """
    Model of the "food_store" table in the database
    """
    designation = models.CharField(max_length=200, unique=True)
    products = models.ManyToManyField(Product, related_name='stores')

    def __str__(self):
        return self.designation

    class Meta:
        verbose_name_plural = "stores"
        
class Comment(models.Model):
    """
    Model of the "food_comment" table in the database
    """
    content = models.TextField(verbose_name='')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='comments')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='comments')
    creation_date = models.DateTimeField(auto_now_add=True)
    deletion_date = models.DateTimeField(null=True, default=None)

    def __str__(self):
        return 'Commentaire {} de {}'.format(self.content, self.user)

    class Meta:
        ordering = ['-creation_date']
