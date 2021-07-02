#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

from .models import User
from .forms import UserCreationForm

# admin.site.register(User, UserAdmin) à utiliser si on ne créé pas son useradmin personnalisé

class UserAdmin(AuthUserAdmin):
    add_form = UserCreationForm
    model = User
