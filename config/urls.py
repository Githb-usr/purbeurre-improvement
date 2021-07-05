#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('user/',include('users.urls'), name='users_urls'),
    path('', include('food.urls'), name='food_urls'),
    path('legal_notices/', TemplateView.as_view(template_name='legal_notices.html'), name='legal_notices'),
    path('admin/', admin.site.urls),
]
