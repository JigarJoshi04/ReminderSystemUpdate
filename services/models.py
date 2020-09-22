from django.db import models
from authentication.models import *
# Create your models here.

class ServiceDateModel(models.Model):
    service_name = models.CharField(max_length=100)
    service_type = models.CharField(max_length=100)
    date_of_deadline = models.DateField()
    actual_date_on_which_reminder_is_to_be_sent = models.DateField()
    recurrence_type = models.IntegerField()


class ClientModel(models.Model):
    id = models.AutoField(primary_key=True, auto_created = True,serialize = False,verbose_name ='ID')
    email = models.CharField(max_length=100)
    client_type = models.CharField(max_length=100)
    staff_id = models.IntegerField()
    ca_name = models.CharField(max_length=100)
    client_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)
    gst = models.CharField(max_length=100)
    aadhar = models.CharField(max_length=100)
    pan = models.CharField(max_length=100)
    income_tax_activate = models.BooleanField(null=False, blank=False)
    gst_tax_activate = models.BooleanField(null=False, blank=False)
    companies_activate = models.BooleanField(null=False, blank=False)
    accounting_activate = models.BooleanField(null=False, blank=False)
    other_service1 = models.BooleanField(null=False, blank=False)
    other_service2 = models.BooleanField(null=False, blank=False)
    other_service3 = models.BooleanField(null=False, blank=False)
    other_service4 = models.BooleanField(null=False, blank=False)
    


