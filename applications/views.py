from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from jobs.models import Job
from .models import Application
from .forms import ApplicationForm


@login_required(login_url="login")
def apply_job(request, job_id):

    profile = request.user.profile

    if profile.role != "JOB_SEEKER":
        return HttpResponseForbidden(
            "Only job seekers can apply."
        )

    job = get_object_or_404(
        Job,
        id=job_id,
        is_active=True
    )

    job_seeker = profile.jobseeker

    # Prevent duplicate applications
    if Application.objects.filter(
        job=job,
        applicant=job_seeker
    ).exists():

        return render(
            request,
            "applications/already_applied.html",
            {
                "job": job
            }
        )

    if request.method == "POST":

        form = ApplicationForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            application = form.save(commit=False)

            application.job = job

            application.applicant = job_seeker

            application.save()

            return redirect(
                "my_applications"
            )

    else:

        form = ApplicationForm()

    return render(
        request,
        "applications/apply_job.html",
        {
            "form": form,
            "job": job
        }
    )
    
    
@login_required(login_url="login")
def my_applications(request):

    profile = request.user.profile

    if profile.role != "JOB_SEEKER":
        return HttpResponseForbidden("Access Denied")

    applications = Application.objects.filter(
        applicant=profile.jobseeker
    ).select_related(
        "job",
        "job__company"
    ).order_by("-applied_at")

    return render(
        request,
        "applications/my_applications.html",
        {
            "applications": applications
        }
    )    
    
    
@login_required(login_url="login")
def applicant_list(request, job_id):

    profile = request.user.profile

    if profile.role != "RECRUITER":
        return HttpResponseForbidden("Access Denied")

    job = get_object_or_404(
        Job,
        id=job_id,
        company__recruiter=profile.recruiter
    )

    applications = Application.objects.filter(
        job=job
    ).select_related(
        "applicant",
        "applicant__user_profile",
        "applicant__user_profile__user"
    )

    return render(
        request,
        "applications/applicant_list.html",
        {
            "job": job,
            "applications": applications
        }
    )    
    
    
@login_required(login_url="login")
def applicant_detail(request, application_id):

    profile = request.user.profile

    if profile.role != "RECRUITER":
        return HttpResponseForbidden("Access Denied")

    application = get_object_or_404(
        Application,
        id=application_id,
        job__company__recruiter=profile.recruiter
    )

    return render(
        request,
        "applications/applicant_detail.html",
        {
            "application": application
        }
    )    
    
    
    
@login_required(login_url="login")
def update_application_status(request, application_id):

    profile = request.user.profile

    if profile.role != "RECRUITER":
        return HttpResponseForbidden("Access Denied")

    application = get_object_or_404(
        Application,
        id=application_id,
        job__company__recruiter=profile.recruiter
    )

    if request.method == "POST":

        application.status = request.POST["status"]

        application.save()

        return redirect(
            "applicant_detail",
            application.id
        )

    return render(
        request,
        "applications/update_status.html",
        {
            "application": application,
            "choices": Application.STATUS_CHOICES
        }
    )    