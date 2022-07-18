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
        widgets = {
            'landCode': forms.TextInput(attrs={'placeholder': 'Land Code'}),
            'ph': forms.NumberInput(attrs={'placeholder': 'pH e.g 7.0'}),
            'size': forms.NumberInput(attrs={'placeholder': 'Land Size in Acres'}),
            'location': forms.TextInput(attrs={'placeholder': 'Location'}),
            'typeOfSoil': forms.TextInput(attrs={'placeholder': 'Type Of Soil'}),
            'soilProperties': forms.TextInput(attrs={'placeholder': 'Soil Properties'}),
            'cost': forms.NumberInput(attrs={'placeholder': 'Cost in Dollars'}),
            'landHistory': forms.TextInput(attrs={'placeholder': 'Land Size in Acres'}),

        }
        fields = ['landCode', 'ph', 'size', 'location', 'typeOfSoil', 'soilProperties', 'cost', 'landHistory', 'primaryImage']


# Form to input data in Image table
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']
