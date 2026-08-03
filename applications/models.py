from django.db import models
from jobs.models import Job
from accounts.models import JobSeekerProfile


class Application(models.Model):

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("SHORTLISTED", "Shortlisted"),
        ("REJECTED", "Rejected"),
        ("HIRED", "Hired"),
    ]

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name="applications"
    )

    applicant = models.ForeignKey(
        JobSeekerProfile,
        on_delete=models.CASCADE,
        related_name="applications"
    )

    cover_letter = models.TextField()

    resume = models.FileField(
        upload_to="applications/resumes/"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    applied_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        unique_together = [
            ("job", "applicant")
        ]

    def __str__(self):
        return f"{self.applicant.user_profile.user.username} - {self.job.title}"
