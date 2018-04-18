# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import bcrypt

# Create your models here.

# Create your models here.
class UserManager(models.Manager):
    def validate(self, postData):
        errors = []
        user = None

        if len(postData['username']) < 1 or len(postData['name']) < 3:
            errors.append("Name and username must be at least 3 characters")
        if postData['password'] != postData['pwconfirm']:
            errors.append("Password and confirm must match")
        if self.filter(username__iexact = postData['username']):
            errors.append("This username already exists in our database.")
        if len(postData['password']) < 8:
            errors.append("Password is too short")

        if not errors:
            user = self.create(
                    username=postData['username'],
                    name=postData['name'],
                    password=bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
                )
        return errors, user
    
    def loginValidate(self, postData):
        errors = []
        user = None

        try:
            user = self.get(username__iexact = postData['username'])
            pw = user.password
            if bcrypt.checkpw(postData['password'].encode(), pw.encode()) == True:
                return errors, user
            else:
                errors.append("Invalid login")
        except:
            errors.append("Invalid login")
        
        return errors, user


class User(models.Model):
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()