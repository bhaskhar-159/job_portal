from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from django.http import HttpResponseForbidden

from .forms import CompanyForm

from .models import Company

from django.shortcuts import render, redirect, get_object_or_404

@login_required(login_url="login")
def create_company(request):

    profile = request.user.profile

    if profile.role != "RECRUITER":

        return HttpResponseForbidden(
            "Only Recruiters can create companies."
        )

    if request.method == "POST":

        form = CompanyForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            company = form.save(commit=False)

            company.recruiter = profile.recruiter

            company.save()

            return redirect(
                "company_list"
            )

    else:

        form = CompanyForm()

    return render(
        request,
        "companies/create_company.html",
        {
            "form": form
        }
    )
    

@login_required(login_url="login")
def company_list(request):

    profile = request.user.profile

    if profile.role != "RECRUITER":
        return HttpResponseForbidden(
            "Only Recruiters can view companies."
        )

    companies = Company.objects.filter(
        recruiter=profile.recruiter
    )

    context = {
        "companies": companies
    }

    return render(
        request,
        "companies/company_list.html",
        context
    )
    

@login_required(login_url="login")
def company_detail(request, company_id):

    profile = request.user.profile

    if profile.role != "RECRUITER":
        return HttpResponseForbidden("Access Denied")

    company = get_object_or_404(
        Company,
        id=company_id,
        recruiter=profile.recruiter
    )

    return render(
        request,
        "companies/company_detail.html",
        {
            "company": company
        }
    )
    
    

@login_required(login_url="login")
def company_update(request, company_id):

    profile = request.user.profile

    if profile.role != "RECRUITER":
        return HttpResponseForbidden("Access Denied")

    company = get_object_or_404(
        Company,
        id=company_id,
        recruiter=profile.recruiter
    )

    if request.method == "POST":

        form = CompanyForm(
            request.POST,
            request.FILES,
            instance=company
        )

        if form.is_valid():

            form.save()

            return redirect(
                "company_detail",
                company.id
            )

    else:

        form = CompanyForm(
            instance=company
        )

    return render(
        request,
        "companies/update_company.html",
        {
            "form": form
        }
    )    
    
    

@login_required(login_url="login")
def company_delete(request, company_id):

    profile = request.user.profile

    if profile.role != "RECRUITER":
        return HttpResponseForbidden("Access Denied")

    company = get_object_or_404(
        Company,
        id=company_id,
        recruiter=profile.recruiter
    )

    if request.method == "POST":

        company.delete()

        return redirect(
            "company_list"
        )

    return render(
        request,
        "companies/delete_company.html",
        {
            "company": company
        }
    )    
    