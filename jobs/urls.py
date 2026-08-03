from django.urls import path
from . import views

urlpatterns = [

    path("company/<int:company_id>/", views.job_list, name="job_list"),
    path( "company/<int:company_id>/create/", views.create_job, name="create_job"),
    path("<int:job_id>/", views.job_detail, name="job_detail"),
    path("<int:job_id>/edit/", views.update_job, name="update_job"),
    path("<int:job_id>/delete/", views.delete_job, name="delete_job"),
    path("browse/", views.browse_jobs, name="browse_jobs"),
    path("browse/<int:job_id>/", views.jobseeker_job_detail, name="jobseeker_job_detail"),

]