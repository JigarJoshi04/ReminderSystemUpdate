from django import forms
from .models import *

# class 
class ClientForm(forms.ModelForm):
    class Meta:
        model = ClientModel
        fields = ['email','client_type','ca_name','staff_id','client_name','phone_no', 'gst', 'aadhar', 'pan','income_tax_activate','gst_tax_activate',
        'companies_activate','accounting_activate','other_service1','other_service2','other_service3','other_service4']
        

class ServiceDateForm(forms.Form):
    class Meta:
        model = ServiceDateModel
        fields = ['service_name','service_type','date_of_deadline','actual_date_on_which_reminder_is_to_be_sent','recurrence_type']
