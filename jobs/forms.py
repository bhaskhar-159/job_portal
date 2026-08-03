from django import forms
from .models import Job


class JobForm(forms.ModelForm):

    class Meta:

        model = Job

        exclude = [
            "company",
            "created_at",
            "updated_at",
        ]

        widgets = {

            "title": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5
            }),

            "requirements": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5
            }),

            "responsibilities": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5
            }),

            "location": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "salary": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "job_type": forms.Select(attrs={
                "class": "form-control"
            }),

            "experience": forms.Select(attrs={
                "class": "form-control"
            }),

            "vacancies": forms.NumberInput(attrs={
                "class": "form-control"
            }),

            "deadline": forms.DateInput(attrs={
                "type": "date",
                "class": "form-control"
            }),

            "is_active": forms.CheckboxInput()
        }