from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Item

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description']
