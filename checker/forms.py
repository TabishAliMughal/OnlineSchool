from django.forms import *
from django import forms
from .models import *

class ManageCheckerCountForm(forms.ModelForm):
    class Meta:
        model = CheckedCount
        fields = [
            'checker',
            'student',
            'exam',
            'count',
        ]