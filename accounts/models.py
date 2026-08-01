from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    ROLE_CHOICES = [
        ("JOB_SEEKER", "Job Seeker"),
        ("RECRUITER", "Recruiter"),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )

    phone = models.CharField(
        max_length=15,
        blank=True
    )

    address = models.TextField(blank=True)

    profile_image = models.ImageField(
        upload_to="profile_images/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.username


class JobSeekerProfile(models.Model):

    user_profile = models.OneToOneField(
        UserProfile,
        on_delete=models.CASCADE,
        related_name="jobseeker"
    )

    resume = models.FileField(
        upload_to="resumes/",
        blank=True,
        null=True
    )

    skills = models.TextField(blank=True)

    education = models.TextField(blank=True)

    experience = models.TextField(blank=True)

    github = models.URLField(blank=True)

    linkedin = models.URLField(blank=True)

    portfolio = models.URLField(blank=True)

    def __str__(self):
        return self.user_profile.user.username


class RecruiterProfile(models.Model):

    user_profile = models.OneToOneField(
        UserProfile,
        on_delete=models.CASCADE,
        related_name="recruiter"
    )

    designation = models.CharField(
        max_length=100,
        blank=True
    )

    department = models.CharField(
        max_length=100,
        blank=True
    )

    def __str__(self):
        return self.user_profile.user.username