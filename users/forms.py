#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import get_user_model

from users.models import Substitute

class UserRegistrationForm(auth_forms.UserCreationForm):
    """
        Form used for the creation of new users
    """

    class Meta(auth_forms.UserCreationForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'username')
