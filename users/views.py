#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm as DjangoUcf
from django.http import HttpResponse
from django.shortcuts import render, redirect
import json

from food.models import Product
from users.forms import UserRegistrationForm
from users.models import User, Substitute
from users.settings import REGISTRATION_ALERT_SUCCESS_MSG, LOGIN_ALERT_SUCCESS_MSG, LOGOUT_MSG, SAVE_SUBSTITUTE_MSG, ALREADY_EXISTS_SUBSTITUTE_MSG, DELETE_SUBSTITUTE_MSG

def registrationView(request):
    """
        We display the registration form
        :return: a template the registration form
    """
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, REGISTRATION_ALERT_SUCCESS_MSG)

            return redirect('login_url')
    else:
        form = UserRegistrationForm()

    return render(request, 'users/registration.html', {'registration_form':form})

def loginView(request):
    """
        We display the login form
        :return: a template with the login form
    """
    messages.success(request, LOGIN_ALERT_SUCCESS_MSG)

    return render(request,'users/login.html')

@login_required()
def dashboardView(request):
    """
        We display the user's dashboard
        :return: a template with the user's informations
    """
    return render(request,'users/dashboard.html')

@login_required()
def savedSubstitutesView(request):
    """
        We display the substitutes favourites page
        :return: a template with all the user's favourites
    """
    favourites = Substitute.objects.all()

    if request.method == "POST":
        # We get the data corresponding to the user's choice
        initial_product_id = request.POST.get('initial-product-id')
        substituted_product_id = request.POST.get('substituted-product-id')
        user_id = request.session['_auth_user_id']
        substitute = Substitute.objects.filter(initial_product_id=initial_product_id, substituted_product_id=substituted_product_id)

        # If the substitute does not already exist in the favourites, it is added.
        if not substitute.exists():
            initial_product = Product.objects.filter(pk=initial_product_id)
            substituted_product = Product.objects.filter(pk=substituted_product_id)
            substitute = Substitute(
                initial_product=initial_product[0],
                substituted_product=substituted_product[0]
            )
            substitute.save()

            user = User.objects.filter(pk=user_id)
            substitute.users.add(user[0])
            # We add a confirmation message
            messages.success(request, SAVE_SUBSTITUTE_MSG)

            return render(request, 'users/my_substitutes.html', { 'favourites': favourites })

        # If the substitute already exist in the favourites, the user is warned.
        messages.success(request, ALREADY_EXISTS_SUBSTITUTE_MSG)
        return render(request, 'users/my_substitutes.html', { 'favourites': favourites })

    # If it's a GET, it simply displays the page with the favourites already saved.
    return render(request, 'users/my_substitutes.html', { 'favourites': favourites })

@login_required()
def deletedSubstitutesView(request):
    """
        We delete a substitute (a favourite)
        :return: an HTTP response to AJAX
    """
    favourites = Substitute.objects.all()

    if request.method == "POST":
        # We get the data corresponding to the user's choice
        body = json.loads(request.body.decode("utf-8"))
        substitute_id = body['substituteId']
        substitute = Substitute.objects.filter(pk=substitute_id)

        # If the substitute to be deleted exists, it is deleted
        if substitute.exists():
            substitute[0].delete()
            # We add a confirmation message
            messages.success(request, DELETE_SUBSTITUTE_MSG)
            # Deleting the substitute from the database generates a status code 204
            return HttpResponse(status=204)
        else:
            # If the substitute does not exist in the database, a 404 status code is generated
            return HttpResponse(status=404)

    # If it's a GET, it simply displays the page with the favourites already saved.
    return HttpResponse(status=301)
