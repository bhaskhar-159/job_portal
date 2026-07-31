from django.db import models
from companies.models import Company


class Job(models.Model):

    JOB_TYPE = [
        ("FULL_TIME", "Full Time"),
        ("PART_TIME", "Part Time"),
        ("INTERNSHIP", "Internship"),
        ("CONTRACT", "Contract"),
    ]

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="jobs"
    )

    title = models.CharField(max_length=200)

    description = models.TextField()

    location = models.CharField(max_length=200)

    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    experience = models.PositiveIntegerField(
        help_text="Years of experience"
    )

    vacancies = models.PositiveIntegerField(default=1)

    job_type = models.CharField(
        max_length=20,
        choices=JOB_TYPE
    )

    deadline = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
