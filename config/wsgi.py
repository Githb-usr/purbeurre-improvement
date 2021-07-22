#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

import dotenv

from django.core.wsgi import get_wsgi_application

dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

env = os.getenv("ENV")
if env == "local":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
elif env == "travis":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.travis')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.prod')

application = get_wsgi_application()
