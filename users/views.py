#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm as DjangoUcf

from food.forms import SearchForm
from users.forms import SavedSubstituteForm, UserCreationForm

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

def registrationView(request):
    """
        We display the xxx
        :return: index template
    """    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request,'registration.html',{'registration_form':form})

@login_required()
def savedSubstitutesView(request):
    """
        We display the xxx
        :return: index template
    """
    form = SavedSubstituteForm()
    
    if request.method == "POST":
        form = SavedSubstituteForm(request.POST)
        print('TOTO', form)
        if form.is_valid():
            new_substitute = form.save()
            messages.success(request, 'Nouveau substitut enregistré en favoris')
            context = {'new_substitute': new_substitute }
            
            return redirect('substitutes', context)

    return render(request,'my_substitutes.html')