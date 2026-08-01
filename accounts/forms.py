from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegistrationForm(forms.ModelForm):
    class Meta:

        model = User

        fields = [
            "username",
            "email",
            "password"
        
        ]
    role = forms.ChoiceField(
    choices=UserProfile.ROLE_CHOICES
)

phone = forms.CharField()    

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Username"
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Password"
        })
    )