from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

"""
    Signal: post_save(): gets fired after User is saved..
    Signal Sender: User
    Signal Receiver: @decorator(signal, sender) > create_profile

    create_profile: a function which runs everytime a User is created decorated with @receiver
"""
# Note:
# Signal receivers are connected in the ready() method of your application configuration class (users > apps.py). Since we're using the receiver() decorator, we need to import the signals submodule inside ready().

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()