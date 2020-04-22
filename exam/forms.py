from django.forms import *
from django import forms
from .models import *

class ManageExamAnswersForm(forms.ModelForm):
    class Meta:
        model = ExamAnswers
        fields = ({
            'student' : forms.IntegerField() ,
            'exam' : forms.IntegerField() ,
            'picture' : forms.ImageField() ,
            'checked' : forms.BooleanField() ,
        })
