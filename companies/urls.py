from django.urls import path
from . import views

urlpatterns = [

    path("create/", views.create_company, name="create_company"),
    path("", views.company_list, name="company_list"),
    path("<int:company_id>/", views.company_detail, name="company_detail"),
    path("<int:company_id>/edit/", views.company_update, name="company_update"),
    path("<int:company_id>/delete/", views.company_delete, name="company_delete"),

]