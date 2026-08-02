from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import UserProfile, JobSeekerProfile, RecruiterProfile
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import (UserRegistrationForm, LoginForm, UserProfileForm, JobSeekerProfileForm, RecruiterProfileForm,)

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
            profile = UserProfile.objects.create(
                user=user,
                role=form.cleaned_data["role"],
                phone=form.cleaned_data["phone"],
            )
            
            # Create role-specific profile
            if profile.role == "JOB_SEEKER":

                JobSeekerProfile.objects.create(
                    user_profile=profile
                )

            elif profile.role == "RECRUITER":

                RecruiterProfile.objects.create(
                    user_profile=profile
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
            
    
@login_required(login_url="login")
def profile(request):

    profile = request.user.profile

    context = {
        "profile": profile
    }

    if profile.role == "JOB_SEEKER":
        context["jobseeker"] = profile.jobseeker

    elif profile.role == "RECRUITER":
        context["recruiter"] = profile.recruiter

    return render(
        request,
        "accounts/profile.html",
        context
    )
    
@login_required(login_url="login")
def edit_profile(request):
    pass    
    


@login_required(login_url="login")
def edit_profile(request):

    profile = request.user.profile

    # -----------------------------
    # JOB SEEKER
    # -----------------------------
    if profile.role == "JOB_SEEKER":

        jobseeker = profile.jobseeker

        if request.method == "POST":

            profile_form = UserProfileForm(
                request.POST,
                request.FILES,
                instance=profile
            )

            jobseeker_form = JobSeekerProfileForm(
                request.POST,
                request.FILES,
                instance=jobseeker
            )

            if profile_form.is_valid() and jobseeker_form.is_valid():

                profile_form.save()
                jobseeker_form.save()

                return redirect("profile")

        else:

            profile_form = UserProfileForm(instance=profile)

            jobseeker_form = JobSeekerProfileForm(instance=jobseeker)

        context = {
            "profile_form": profile_form,
            "role_form": jobseeker_form,
        }

        return render(
            request,
            "accounts/edit_profile.html",
            context
        )

    # -----------------------------
    # RECRUITER
    # -----------------------------
    recruiter = profile.recruiter

    if request.method == "POST":

        profile_form = UserProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        recruiter_form = RecruiterProfileForm(
            request.POST,
            instance=recruiter
        )

        if profile_form.is_valid() and recruiter_form.is_valid():

            profile_form.save()
            recruiter_form.save()

            return redirect("profile")

    else:

        profile_form = UserProfileForm(instance=profile)

        recruiter_form = RecruiterProfileForm(instance=recruiter)

    context = {

        "profile_form": profile_form,

        "role_form": recruiter_form,
    }

    return render(
        request,
        "accounts/edit_profile.html",
        context
    )    