#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
import logging

from errors import DatabaseError
from food.database_service import DatabaseService
from food.models import Product, Category, Store

# Get an instance of a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class Command(BaseCommand):
    help = 'Extract data from the Open Food Fact API for populate the database'

    def handle(self, *args, **options):
        """
            We populate the database with data retrieved via the Open Food Facts API
        """
        try:
            database_service = DatabaseService()
            self.stdout.write(self.style.WARNING(
                "Téléchargement des données depuis l'API d'Open Food Facts"
            ))
            # Extract raw data from API
            database_service.get_api_data()
            self.stdout.write(self.style.WARNING(
                "Insertion des données Open Food Facts dans la base Pur Beurre en cours"
            ))
            # Populate product table
            database_service.populate_database_with_products()
            # Populate category table
            database_service.populate_database_with_categories()
            # Populate category-products table
            database_service.populate_database_with_category_products()
            # Populate store table
            database_service.populate_database_with_stores()
            # Populate store-products table
            database_service.populate_database_with_store_products()
            self.stdout.write(self.style.SUCCESS(
                "Insertion des données réussie !"
            ))
            logger.info(
                "L'insertion des données Open Food Facts dans la base Pur Beurre est un succès !",
                exc_info=True
                )
        except DatabaseError:
            self.stderr.write(self.style.ERROR("L'insertion des données a échoué..."))
            logger.error(
                "L'insertion des données Open Food Facts dans la base Pur Beurre est un échec...",
                exc_info=True
                )
