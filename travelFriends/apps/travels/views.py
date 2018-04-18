# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def travels_index(request):
    if not 'user_id' in request.session:
        return redirect("/")
    else:
        context = {
            'user': User.objects.get(id=request.session['user_id']),
            'trips': Trip.objects.all().exclude(createor__id=request.session['user_id']).exclude(users__id=request.session['user_id'])
        }
    return render(request, 'travels/travels.html', context)

def add_travel_plan(request):
    if not 'user_id' in request.session:
        return redirect("/")
    else:
        context = {
            'user': User.objects.get(id=request.session['user_id'])
        }
        return render(request, 'travels/add_travel_plan.html', context)

def process_trip(request):
    validations = Trip.objects.validate(request.POST)
    this_trip = validations[1]
    print this_trip
    this_user = User.objects.get(id=request.session['user_id'])

    if len(validations[0]) == 0:
        print "no errors============"
        print request.POST
        this_trip.createor=this_user
        this_trip.users.add(this_user)
        this_trip.save()
        return redirect("/travels")
    else:
        for error in validations[0]:
            messages.add_message(request, messages.INFO, error)
            print error
        return redirect("/travels/add_travel_plan")
    
def view_trip(request, id):
    if not 'user_id' in request.session:
        return redirect("/")
    else:
        this_trip = Trip.objects.get(id=id)
        this_captain = this_trip.createor.id
        context = {
            'trip': Trip.objects.get(id=id),
            'other_users': User.objects.filter(trips=this_trip).exclude(id=this_captain)
        }
        return render(request, 'travels/view_trip.html', context)

def join_trip(request, id):
    this_trip = Trip.objects.get(id=id)
    this_user = User.objects.get(id=request.session['user_id'])
    this_id = this_user.id

    if  len(this_trip.users.filter(id=this_id)) > 0:
        messages.add_message(request, messages.INFO, "You are already going on this trip!")
        return redirect("/travels")
    
    else:
        this_trip.users.add(this_user)
        return redirect("/travels/"+str(id))
# t1.users.get(username="alexkenta")