from django import forms
from django.contrib.auth.models import User
from .models import Profile, Hood, Business, News


class EditProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    exclude = ('user', 'location')

class BusinessForm(forms.ModelForm):
  class Meta:
    model = Business
    exclude = ('owner', 'hood')

class HoodForm(forms.ModelForm):
    class Meta:
        model = Hood
        exclude = ('admin',)

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        exclude = ('user', 'hood')