# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def index(request):
    request.session.clear()
    return render(request, 'log_reg/index.html')

def process_registration(request):
    validation = User.objects.validate(request.POST)
    
    if len(validation[0]) > 0:
        for error in validation[0]:
            messages.add_message(request, messages.INFO, error) 
            print "failure to register======="          
        return redirect("/")
    else:
        request.session['user_id'] = validation[1].id
        print request.session['user_id']
        print "successful registration======"
        return redirect("/travels")

def process_login(request):
    validation = User.objects.loginValidate(request.POST)

    if len(validation[0]) > 0:
        for error in validation[0]:
            messages.add_message(request, messages.INFO, error)   
            print "failure to login====="        
        return redirect("/")
    else:
        request.session['user_id'] = validation[1].id
        print request.session['user_id']
        print "successfull login====="
        return redirect("/travels")

def logout(request):
    request.session.clear()
    return redirect("/")
    
