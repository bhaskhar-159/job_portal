from django import forms
from .models import Company


from django import forms
from .models import Company


class CompanyForm(forms.ModelForm):

    class Meta:

        model = Company

        fields = [
            "name",
            "description",
            "website",
            "email",
            "phone",
            "location",
            "logo"
        ]

        widgets = {

            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Company Name"
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5
            }),

            "website": forms.URLInput(attrs={
                "class": "form-control"
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control"
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "location": forms.TextInput(attrs={
                "class": "form-control"
            }),

        }