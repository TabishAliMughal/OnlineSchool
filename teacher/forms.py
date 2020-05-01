from django.forms import *
from django import forms
from .models import *

class TeacherClassStudentCreateForm(forms.ModelForm):
    class Meta:
        model = TeacherClassStudents
        fields = [
            'id' ,
            'clas' ,
            'name' ,
            'father_name' ,
            'contact' ,
            'address' ,
            'picture' ,
        ]

class TeacherClassCreateForm(forms.ModelForm):
    class Meta:
        model = TeacherClass
        fields = [
            'teacher' ,
            'clas' ,
            'limit' ,
            'school',
        ]


from location_field.forms.plain import PlainLocationField
class Address(forms.Form):
    city = forms.CharField()
    location = PlainLocationField(based_fields=['city'],
        initial='-22.2876834,-49.1607606')