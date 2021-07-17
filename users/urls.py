#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.views import LoginView,LogoutView
from django.urls import path

from users.settings import LOGIN_ALERT_SUCCESS_MSG, LOGOUT_MSG

from . import views

urlpatterns = [
    path('registration/', views.registrationView, name='registration_url'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login_url'),
    path('dashboard/', views.dashboardView, name="dashboard"),
    path('my_substitutes/', views.saved_substitutes_view, name='substitutes'),
    path('delete_substitutes/', views.deleted_substitutes_view, name='delete_substitutes'),
    path('logout/', LogoutView.as_view(), name='logout'),
]