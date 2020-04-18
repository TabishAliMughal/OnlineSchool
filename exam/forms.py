from django.forms import *
from django import forms
from .models import *

class ManageExamAnswersForm(forms.ModelForm):
    class Meta:
        model = ExamAnswers
        fields = [
            'student' ,
            'exam' ,
            'picture' ,
        ]
