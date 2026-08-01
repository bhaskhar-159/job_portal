from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import UserProfile
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

def register(request):
    
    # If the user submits the registration form
    if request.method == "POST":
        
        # Get the submitted data
        form = UserRegistrationForm(request.POST)
        
        # Validate the form
        if form.is_valid():
            
            # Create the object but don't save yet
            user = form.save(commit=False)
            
            # Hash the password
            user.set_password(form.cleaned_data["password"])
            
            # Save user in auth_user table
            user.save()
            
            # Create UserProfile
            UserProfile.objects.create(
                user=user,
                role=form.cleaned_data["role"],
                phone=form.cleaned_data["phone"],
            )
            
            # Redirect to login page
            return redirect("login")
    else:
        # User is visiting the page for the first time they have to register in the form
        form = UserRegistrationForm()
        
    return render(request, "accounts/register.html", {"form": form})
                
        
    
def user_login(request):

    if request.method == "POST":

        form = LoginForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:

                login(request, user)

                # Role-Based Redirection

                if user.profile.role == "RECRUITER":
                    return redirect("recruiter_dashboard")

                elif user.profile.role == "JOB_SEEKER":
                    return redirect("jobseeker_dashboard")

            else:
                form.add_error(None, "Invalid Username or Password")

    else:
        form = LoginForm()

    return render(
        request,
        "accounts/login.html",
        {"form": form}
    )
    

def user_logout(request):
    logout(request)
    return redirect("login")    
    
    
    
@login_required(login_url="login")
def recruiter_dashboard(request):

    if request.user.profile.role != "RECRUITER":
        return HttpResponseForbidden("Access Denied")

    return render(
        request,
        "accounts/recruiter_dashboard.html"
    )
    
@login_required(login_url="login")
def jobseeker_dashboard(request):

    if request.user.profile.role != "JOB_SEEKER":
        return HttpResponseForbidden("Access Denied")

    return render(
        request,
        "accounts/jobseeker_dashboard.html"
    )            
            
    
   
    
    