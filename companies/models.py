from django.db import models
from accounts.models import RecruiterProfile


class Company(models.Model):

    recruiter = models.ForeignKey(
    RecruiterProfile,
    on_delete=models.CASCADE,
    related_name="companies",
    null=True,
    blank=True
)

    name = models.CharField(max_length=200)

    description = models.TextField()

    website = models.URLField(blank=True)

    email = models.EmailField(blank=True)

    phone = models.CharField(max_length=15, blank=True)

    location = models.CharField(max_length=200)

    logo = models.ImageField(
        upload_to="company_logos/",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name