from django import forms
from .models import Application


class ApplicationForm(forms.ModelForm):

    class Meta:

        model = Application

        fields = [
            "cover_letter",
            "resume",
        ]

        widgets = {

            "cover_letter": forms.Textarea(
                attrs={
                    "rows": 8,
                    "class": "form-control"
                }
            )
        }