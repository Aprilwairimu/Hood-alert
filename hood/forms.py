from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django import forms
from django.forms import ModelForm
from .models import Profile, NeighbourHood, Business, Post

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username","email","password1","password2"]

class LoginForm(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.CharField(max_length=20, widget=forms.PasswordInput)

class NeighbourHoodForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        exclude = ('admin',)


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('user', 'neighbourhood')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('__all__')

class ProfileForm(ModelForm):
    class Meta:
        model= Profile
        # fields= "__all__"
        fields=('user','name', 'bio','profile_picture', 'location', 'neighbourhood')

        labels={
            'user':'user',
            'name':'name',
            'bio':'bio',
            'profile_picture':'profile_picture',
            'location':'location',
            'neighbourhood':'neighbourhood',   

        }

        widgets={
           'user':forms.Textarea(attrs={'class': 'form-control','placeholder':'user'}),

           'name': forms.TextInput(attrs={'class': 'form-control','placeholder':'  name '}),

           'bio':forms.Textarea(attrs={'class': 'form-control','placeholder':'bio'}),

           'location':forms.Textarea(attrs={'class': 'form-control','placeholder':'location'}),

           'neighbourhood': forms.Textarea(attrs={'class': 'form-control','placeholder':'neighbourhood '}),
           

        }