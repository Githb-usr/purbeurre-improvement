#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm as DjangoUcf
from django.http import HttpResponse
from django.shortcuts import render, redirect
import json

from food.models import Product
from users.forms import UserCreationForm
from users.models import User, Substitute
from users.settings import REGISTRATION_ALERT_SUCCESS_MSG, LOGIN_ALERT_SUCCESS_MSG, LOGOUT_MSG, SAVE_SUBSTITUTE_MSG, ALREADY_EXISTS_SUBSTITUTE_MSG, DELETE_SUBSTITUTE_MSG

def registrationView(request):
    """
        We display the xxx
        :return: index template
    """    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, REGISTRATION_ALERT_SUCCESS_MSG)
            
            return redirect('login_url')
    else:
        form = UserCreationForm()

    return render(request, 'registration.html', {'registration_form':form})

def loginView(request):
    """
        We display the xxx
        :return: index template
    """    
    messages.success(request, LOGIN_ALERT_SUCCESS_MSG)
    
    return render(request,'login.html')

@login_required()
def dashboardView(request):
    """
        We display the xxx
        :return: index template
    """  
    return render(request,'dashboard.html')

@login_required()
def savedSubstitutesView(request):
    """
        We display the xxx
        :return: index template
    """
    favourites = Substitute.objects.all()
            
    if request.method == "POST":
        initial_product_id = request.POST.get('initial-product-id')
        substituted_product_id = request.POST.get('substituted-product-id')
        user_id = request.session['_auth_user_id']
        substitute = Substitute.objects.filter(initial_product_id=initial_product_id, substituted_product_id=substituted_product_id)

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

            messages.success(request, SAVE_SUBSTITUTE_MSG)
            return render(request, 'my_substitutes.html', { 'favourites': favourites })

        messages.success(request, ALREADY_EXISTS_SUBSTITUTE_MSG)
        return render(request, 'my_substitutes.html', { 'favourites': favourites })
    
    return render(request, 'my_substitutes.html', { 'favourites': favourites })

@login_required()
def deletedSubstitutesView(request):
    """
        We display the xxx
        :return: xxx template
    """
    
    favourites = Substitute.objects.all()
    
    if request.method == "POST":
        print('hello')
        body = json.loads(request.body.decode("utf-8"))
        print(body)
        substitute_id = body['substituteId']
        print(substitute_id)
        substitute = Substitute.objects.filter(pk=substitute_id)
        print(substitute)
        if substitute.exists():
            substitute[0].delete()
            messages.success(request, DELETE_SUBSTITUTE_MSG)
            print("deleted")
            return HttpResponse(status=204)
        else:
            print("not found")
            return HttpResponse(status=404)
    print("301")
    return HttpResponse(status=301)
