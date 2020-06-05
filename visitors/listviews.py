from django.shortcuts import render
from . models import *

def ManageTeacherVisitListView(ListView):
    user = ListView.user.groups.values('name')
    Teachers = TeacherVisit.objects.all()
    context = {
        'Teachers' : Teachers ,
        'user' : user ,
    }
    return render(ListView , 'Visits/Teacher/list.html' , context)

def ManageSchoolVisitListView(ListView):
    user = ListView.user.groups.values('name')
    Schools = SchoolVisit.objects.all()
    context = {
        'Schools' : Schools ,
        'user' : user ,
    }
    return render(ListView , 'Visits/School/list.html' , context)

def ManageParentVisitListView(ListView):
    user = ListView.user.groups.values('name')
    Parents = ParentVisit.objects.all()
    context = {
        'Parents' : Parents ,
        'user' : user ,
    }
    return render(ListView , 'Visits/Parent/list.html' , context)

