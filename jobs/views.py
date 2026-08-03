from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import JobForm
from companies.models import Company
from django.shortcuts import get_object_or_404
from .models import Job
from django.db.models import Q


@login_required(login_url="login")
def create_job(request, company_id):

    profile = request.user.profile

    if profile.role != "RECRUITER":
        return HttpResponseForbidden("Access Denied")

    company = get_object_or_404(
        Company,
        id=company_id,
        recruiter=profile.recruiter
    )

    if request.method == "POST":

        form = JobForm(
            request.POST
        )

        if form.is_valid():

            job = form.save(commit=False)

            job.company = company

            job.save()

            return redirect(
                "job_list",
                company.id
            )

    else:

        form = JobForm()

    return render(
        request,
        "jobs/create_job.html",
        {
            "form": form,
            "company": company
        }
    )



@login_required(login_url="login")
def job_list(request, company_id):

    profile = request.user.profile

    if profile.role != "RECRUITER":
        return HttpResponseForbidden("Access Denied")

    company = get_object_or_404(
        Company,
        id=company_id,
        recruiter=profile.recruiter
    )

    jobs = Job.objects.filter(
        company=company
    )

    context = {
        "company": company,
        "jobs": jobs
    }

    return render(
        request,
        "jobs/job_list.html",
        context
    )
  

@login_required(login_url="login")
def job_detail(request, job_id):

    profile = request.user.profile

    if profile.role != "RECRUITER":
        return HttpResponseForbidden("Access Denied")

    job = get_object_or_404(
        Job,
        id=job_id,
        company__recruiter=profile.recruiter
    )

    return render(
        request,
        "jobs/job_detail.html",
        {
            "job": job
        }
    )    
    
    
@login_required(login_url="login")
def update_job(request, job_id):

    profile = request.user.profile

    if profile.role != "RECRUITER":
        return HttpResponseForbidden("Access Denied")

    job = get_object_or_404(
        Job,
        id=job_id,
        company__recruiter=profile.recruiter
    )

    if request.method == "POST":

        form = JobForm(
            request.POST,
            instance=job
        )

        if form.is_valid():

            updated_job = form.save(commit=False)
            updated_job.company = job.company
            updated_job.save()

            return redirect(
                "job_detail",
                job.id
            )

    else:

        form = JobForm(
            instance=job
        )

    return render(
        request,
        "jobs/update_job.html",
        {
            "form": form,
            "job": job
        }
    )  
    
    
    
@login_required(login_url="login")
def delete_job(request, job_id):

    profile = request.user.profile

    if profile.role != "RECRUITER":
        return HttpResponseForbidden("Access Denied")

    job = get_object_or_404(
        Job,
        id=job_id,
        company__recruiter=profile.recruiter
    )

    company_id = job.company.id

    if request.method == "POST":

        job.delete()

        return redirect(
            "job_list",
            company_id
        )

    return render(
        request,
        "jobs/delete_job.html",
        {
            "job": job
        }
    )      
    
    
    
@login_required(login_url="login")
def browse_jobs(request):

    profile = request.user.profile

    if profile.role != "JOB_SEEKER":
        return HttpResponseForbidden(
            "Access Denied"
        )

    search = request.GET.get("search")

    jobs = Job.objects.filter(
        is_active=True
    ).select_related("company")

    if search:

        jobs = jobs.filter(

            Q(title__icontains=search) |
            Q(company__name__icontains=search) |
            Q(location__icontains=search)

        )

    context = {

        "jobs": jobs,
        "search": search

    }

    return render(
        request,
        "jobs/browse_jobs.html",
        context
    )    
    
    

@login_required(login_url="login")
def jobseeker_job_detail(request, job_id):

    profile = request.user.profile

    if profile.role != "JOB_SEEKER":

        return HttpResponseForbidden(
            "Access Denied"
        )

    job = get_object_or_404(

        Job,

        id=job_id,

        is_active=True

    )

    return render(

        request,

        "jobs/jobseeker_job_detail.html",

        {

            "job": job

        }

    )    