from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, JobSeekerProfile, RecruiterProfile

class UserRegistrationForm(forms.ModelForm):
    
    role = forms.ChoiceField(
        choices=UserProfile.ROLE_CHOICES
    )    
    
    phone = forms.CharField()
    
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        
    password = forms.CharField(
        widget=forms.PasswordInput()    
        
)

    

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
    
class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ["phone", "address", "profile_image"]    
        
        
class JobSeekerProfileForm(forms.ModelForm):

    class Meta:
        model = JobSeekerProfile
        fields = ["resume", "skills", "education", "experience", "github", "linkedin", "portfolio"] 
        

class RecruiterProfileForm(forms.ModelForm):

    class Meta:
        model = RecruiterProfile
        fields = ["designation", "department"]               