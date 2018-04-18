# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..log_reg.models import *
from django.db import models
from datetime import datetime


today = str(datetime.now().date())
today_date = datetime.strptime(today, '%Y-%m-%d')
# Create your models here.
class TripValidate(models.Manager):
    def validate(self, postData):
        errors =[]
        this_trip = None

        if len(postData['destination']) < 1 or len(postData['plan']) < 1 or len(postData['start_date']) < 1 or len(postData['end_date']) < 1:
            errors.append("All fields must be filled out to book a trip")
        if not postData['end_date'] > postData['start_date']:
            errors.append("You cannot leave a place before you arrive at a place")
        if not str(postData['start_date']) > str(today_date):
            errors.append("You cannot take a trip into the past")
        if not errors:
            this_trip = self.create(
                destination = postData['destination'],
                plan = postData['plan'],
                start_date = postData['start_date'],
                end_date=postData['end_date'],
            )
        print today
        return errors, this_trip


class Trip(models.Model):
    destination = models.CharField(max_length=255)
    plan = models.TextField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    createor = models.ForeignKey(User, default=1, null=True)
    users = models.ManyToManyField(User, related_name="trips")
    objects = TripValidate()