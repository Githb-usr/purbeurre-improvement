#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

from .models import User
from .forms import UserRegistrationForm

# admin.site.register(User, UserAdmin) à utiliser si on ne créé pas son useradmin personnalisé

class UserAdmin(AuthUserAdmin):
    """
        Display of users in the back office
    """
    add_form = UserRegistrationForm
    model = User
