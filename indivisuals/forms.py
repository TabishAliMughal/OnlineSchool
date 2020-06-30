from django import *
from django import forms
from django.forms import ModelForm
from .models import *
from requirments.models import *


class IndivisualsForm(forms.ModelForm):
    class Meta:
        model = Indivisuals
        fields = [
            'user' ,
            'session',
            'name' ,
            'father_name' ,
            'mobile' ,
            'school' ,
            'clas' ,
            'fees' ,
            'password',
            'active' ,
        ]
