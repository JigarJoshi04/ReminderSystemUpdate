from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from authentication.models import *


class CAForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email','password')

class StaffForm(forms.ModelForm):
    class Meta:
        model = StaffModel
        fields = ('ca_name', 'phone_no', 'repassword')




