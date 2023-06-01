from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django import forms
 
class RegisterForm(UserCreationForm) :
    first_name = forms.CharField(max_length=32 )                                 #adding custom fields
    last_name = forms.CharField(max_length=32) 
    class Meta:
        model = User                                                             #adding to User in database
        fields = ['username','email','password1','password2']

       