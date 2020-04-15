from django import *
from django import forms
from django.forms import ModelForm
from .models import *
from requirments.models import *


class ClassesForm(forms.ModelForm):
    class Meta:
        model = Classes
        fields = [
            'class_name',
        ]

class SubjectsForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = [
            'subject_name',
        ]

class ClassSubjectsForm(forms.ModelForm):
    class Meta:
        model = ClassSubjects
        fields = [
            'class_name',
            'subject_name',
        ]

class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = [
            'module',
        ]

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = [
            'class_name',
            'subject',
            'module',
            'date',
            'title',
            'text',
            'url',
        ]
