from django.shortcuts import render , redirect
from . models import *
from .forms import *

def ManageTeacherVisitCreateView(CreateView):
    user = CreateView.user.groups.values('name')
    if CreateView.method == 'POST':
        form = ManageTeacherVisitForm(CreateView.POST)
        if form.is_valid:
            form.save()
            return redirect('main')
    else:
        form = ManageTeacherVisitForm()
        context = {
            'form': form ,
            'user' : user ,
        }
        return render(CreateView , 'Visits/Teacher/Create.html',context)

def ManageSchoolVisitCreateView(CreateView):
    user = CreateView.user.groups.values('name')
    if CreateView.method == 'POST':
        form = ManageSchoolVisitForm(CreateView.POST)
        if form.is_valid:
            form.save()
            return redirect('main')
    else:
        form = ManageSchoolVisitForm()
        context = {
            'form': form ,
            'user' : user ,
        }
        return render(CreateView , 'Visits/School/Create.html',context)

def ManageParentVisitCreateView(CreateView):
    user = CreateView.user.groups.values('name')
    if CreateView.method == 'POST':
        form = ManageParentVisitForm(CreateView.POST)
        if form.is_valid:
            form.save()
            return redirect('main')
    else:
        form = ManageParentVisitForm()
        context = {
            'form': form ,
            'user' : user ,
        }
        return render(CreateView , 'Visits/Parent/Create.html',context)
