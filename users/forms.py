#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm, HiddenInput

from users.models import Substitute

class UserCreationForm(auth_forms.UserCreationForm):
    """
        Form used for the creation of new users
    """
    
    class Meta(auth_forms.UserCreationForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'username')

class SavedSubstituteForm(forms.ModelForm):
    """
        Form used for the creation of new users
    """

    class Meta:
        model = Substitute
        fields = ['users', 'initial_product', 'substituted_product']
        widgets = {
            'users': forms.HiddenInput(attrs={
                        "id": "user-id",
                        "name": "user-id",
                        "value": "{{ request.user.pk }}",
                    }),
            'initial_product': forms.HiddenInput(attrs={
                        "id": "initial-product-id",
                        "name": "initial-product-id",
                        "value": "{{ initial_product.id }}",
                    }),
            'substituted_product': forms.HiddenInput(attrs={
                        "id": "substitute-id",
                        "name": "substitute-id",
                        "value": "{{ substitute.id }}",
                    }),
                }
