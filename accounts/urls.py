from django.urls import path
from . import views

urlpatterns = [

    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),

    path("recruiter-dashboard/", views.recruiter_dashboard, name="recruiter_dashboard"),

    path("jobseeker-dashboard/", views.jobseeker_dashboard, name="jobseeker_dashboard"),


]