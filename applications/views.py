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