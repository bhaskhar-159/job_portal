from django.db import models
from companies.models import Company


class Job(models.Model):

    JOB_TYPE_CHOICES = [
        ("FULL_TIME", "Full Time"),
        ("PART_TIME", "Part Time"),
        ("INTERNSHIP", "Internship"),
        ("CONTRACT", "Contract"),
    ]

    EXPERIENCE_CHOICES = [
        ("FRESHER", "Fresher"),
        ("1-3", "1-3 Years"),
        ("3-5", "3-5 Years"),
        ("5+", "5+ Years"),
    ]

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="jobs"
    )

    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    requirements = models.TextField()

    responsibilities = models.TextField()

    location = models.CharField(
        max_length=200
    )

    salary = models.CharField(
        max_length=100
    )

    job_type = models.CharField(
        max_length=20,
        choices=JOB_TYPE_CHOICES
    )

    experience = models.CharField(
        max_length=20,
        choices=EXPERIENCE_CHOICES
    )

    vacancies = models.PositiveIntegerField()

    deadline = models.DateField()

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title