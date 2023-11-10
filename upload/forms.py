from django import forms
from .models import AssignmentSubmission


class TaskSubmissionForm(forms.ModelForm):
    class Meta:
        model = AssignmentSubmission
        fields = ['user', 'file']