# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class StaffModel(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True,)
    ca_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=10)
    repassword = models.CharField(max_length=100)


    

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

