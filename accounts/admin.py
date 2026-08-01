from django.contrib import admin
from .models import UserProfile, JobSeekerProfile, RecruiterProfile

admin.site.register(UserProfile)
admin.site.register(JobSeekerProfile)
admin.site.register(RecruiterProfile)
