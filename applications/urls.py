from django.urls import path
from . import views

urlpatterns = [

    path("apply/<int:job_id>/", views.apply_job, name="apply_job"),
    path("my/", views.my_applications, name="my_applications"),
    path("job/<int:job_id>/applicants/", views.applicant_list, name="applicant_list"),
    path("<int:application_id>/", views.applicant_detail, name="applicant_detail"),
    path("<int:application_id>/status/", views.update_application_status, name="update_application_status"),

]