from django import forms
from django.contrib.auth.models import User
from .models import *

class userRegisterForm(forms.Form):
    user_name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'Username'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email Address'}))
    first_name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    last_name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
    password1=forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2=forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'placeholder':'password (again)'}))

    def clean_user_name(self):
        user=self.cleaned_data['user_name']
        if User.objects.filter(username=user).exists():
            raise forms.ValidationError('User already exists!')
        return user
    def clean_email(self):
        email=self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('email already exists!')
        return email
    def clean_password2(self):
        password1=self.cleaned_data['password1']
        password2=self.cleaned_data['password2']
        if len(password2)<8:
            raise forms.ValidationError('Password must be more than 8 chars!')
        elif password1 != password2:
            raise forms.ValidationError('Password Not Match!')
        return password2

class userLoginForm(forms.Form):
    username=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password=forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['email','first_name','last_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['Phone','profile_image']
