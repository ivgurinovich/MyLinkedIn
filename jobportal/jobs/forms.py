from django import forms
from .models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'location', 'salary', 'description', 'job_type', 'is_active']
