# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    STUDENT = 1
    TEACHER = 2
    SUPERVISOR = 3
    ROLE_CHOICE = (
            (STUDENT,'Student'),
            (TEACHER,'Teacher'),
            (SUPERVISOR,'Supervisor'),
            )
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(max_length=500,blank=True)
    location = models.CharField(max_length=30,blank=True)
    birth_date = models.DateField(null=True,blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE,null=True,blank=True)

    def __unicode__(self): # __unicode__ for Python 2
        return self.user.username

@receiver(post_save,sender=User)
def create_or_update_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

# @receiver(post_save,sender=User)
# def save_user_profile(sender,instance,**kwargs):
    # instance.profile.save()
