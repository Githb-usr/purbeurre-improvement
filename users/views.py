#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm as DjangoUcf

from food.forms import SearchForm
from users.forms import UserCreationForm as CustomUcf

def loginView(request):
    """
        We display the xxx
        :return: index template
    """    
    search_form = SearchForm()
    
    return render(request,'login.html', { 'search_form': search_form })

@login_required()
def dashboardView(request):
    """
        We display the xxx
        :return: index template
    """
    search_form = SearchForm()
    
    return render(request,'dashboard.html', { 'search_form': search_form })

def registrationView(request):
    """
        We display the xxx
        :return: index template
    """
    search_form = SearchForm()
    
    if request.method == "POST":
        form = CustomUcf(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = CustomUcf()
    return render(request,'registration.html',{'search_form': search_form, 'registration_form':form})

def substitutesView(request):
    """
        We display the xxx
        :return: index template
    """
    search_form = SearchForm()
    
    return render(request,'my_substitutes.html', { 'search_form': search_form })