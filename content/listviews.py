from django.shortcuts import render , redirect , get_object_or_404 , get_list_or_404
from requirments.models import *
from .models import *

def ManageClassListView(ListView):
    list_ = Classes.objects.all()
    user = ListView.user.groups.values('name')
    context = {
        'list':list_,
        'user':user ,
    }
    return render (ListView,'Lists/classes.html',context)

def ManageContentListView(ListView):
    list_ = Content.objects.all()
    user = ListView.user.groups.values('name')
    context = {
        'list':list_,
        'user':user ,
    }
    return render (ListView,'Lists/content.html',context)

def ManageSubjectListView(ListView):
    list_ = Subjects.objects.all()
    user = ListView.user.groups.values('name')
    context = {
        'list':list_,
        'user':user ,
    }
    return render (ListView,'Lists/subjects.html',context)

def ManageModuleListView(ListView):
    list_ = Module.objects.all()
    user = ListView.user.groups.values('name')
    context = {
        'list':list_,
        'user':user ,
    }
    return render (ListView,'Lists/module.html',context)

def ManageClassSubjectsListView(ListView):
    list_ = ClassSubjects.objects.all()
    user = ListView.user.groups.values('name')
    context = {
        'list':list_,
        'user':user ,
    }
    return render (ListView,'Lists/classsubjects.html',context)

