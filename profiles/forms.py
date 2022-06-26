from django import forms
from .models import *
from django.contrib.auth.models import User
class UserUpdateForm(forms.ModelForm):
   username = forms.CharField(max_length=100,required=True)
   email = forms.EmailField(required=True)
   class Meta:
    model = User
    fields = ("username","email")

class ProfileUpdateForm(forms.ModelForm):
   img = forms.ImageField()
   class Meta:
      model = Profile
      fields = ["img"]