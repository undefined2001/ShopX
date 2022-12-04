from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class MyUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':' Enter Your Name'}))
    password1 = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':' Enter Your Password'}))
    password2 = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':' Retype Your Password'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Your Email'}))
    phone_number = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Phone Number'}))

    class Meta:
        model = User
        fields = ["username", "email", "phone_number", "password1", "password2"]