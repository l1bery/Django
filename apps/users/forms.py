from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

CustomUser = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['username','email']
        widgets = {
            'username': forms.TextInput(attrs={'size': '40'}),
            'email': forms.EmailInput(attrs={'size': '40'}),
        }