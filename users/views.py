#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm as DjangoUcf
from django.shortcuts import render, redirect

from food.models import Product
from users.forms import UserCreationForm
from users.models import User, Substitute

def registrationView(request):
    """
        We display the xxx
        :return: index template
    """    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre compte a bien été créé, vous pouvez vous connecter.')
            return redirect('login_url')
    else:
        form = UserCreationForm()

    return render(request, 'registration.html', {'registration_form':form})

def loginView(request):
    """
        We display the xxx
        :return: index template
    """    
   
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
        print('XXXXX', initial_product_id)
        substituted_product_id = request.POST.get('substituted-product-id')
        print('IIIII', substituted_product_id)
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

            messages.success(request, 'Nouveau substitut enregistré en favoris')
            return render(request, 'my_substitutes.html', { 'favourites': favourites })

        messages.success(request, 'Ce substitut existe déjà, il n\'a donc pas été enregistré')
        return render(request, 'my_substitutes.html', { 'favourites': favourites })
    
    return render(request, 'my_substitutes.html', { 'favourites': favourites })

@login_required()
def deletedSubstitutesView(request):
    """
        We display the xxx
        :return: xxx template
    """
    
    favourites = Substitute.objects.all()
    for fav in favourites:
        print(fav.id)
    
    if request.method == "POST":
        substitute_id = request.POST.get('substitute-id')
        print('AAA', substitute_id)
        substitute = Substitute.objects.filter(pk=substitute_id)
        print('BBB', substitute)
        if substitute.exists():
            substitute[0].delete()

            messages.success(request, 'Le substitut a été supprimé')
            return render(request, 'my_substitutes.html', { 'favourites': favourites })

    return render(request, 'my_substitutes.html', { 'favourites': favourites })
