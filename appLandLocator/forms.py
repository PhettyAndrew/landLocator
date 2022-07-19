from django import forms
from django.contrib.auth.models import User
from .models import Land, Image


# User data input form
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


# Form to input data in Land table
class LandForm(forms.ModelForm):
    class Meta:
        model = Land
        fields = ['landCode', 'ph', 'size', 'location', 'typeOfSoil', 'soilProperties', 'cost', 'landHistory', 'primaryImage']


# Form to input data in Image table
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']
