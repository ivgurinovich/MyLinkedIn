from django import forms
from .models import Resume, Application


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['title', 'experience', 'education', 'skills']


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['cover_letter']
