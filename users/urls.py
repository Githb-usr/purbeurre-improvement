#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.views import LoginView,LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path('registration/', views.registrationView, name="registration_url"),
    path('login/', LoginView.as_view(template_name="login.html", redirect_field_name='/'), name="login_url"),
    path('dashboard/', views.dashboardView, name="dashboard"),
    path('substitutes/', views.substitutesView, name="substitutes"),
    path('logout/', LogoutView.as_view(redirect_field_name='/'), name="logout"),
]