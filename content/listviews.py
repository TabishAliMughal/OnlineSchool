from django.shortcuts import render , redirect , get_object_or_404 , get_list_or_404
from requirments.models import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group , User
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only
import datetime
from datetime import timedelta


@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def ManageClassListView(ListView):
    list_ = Classes.objects.all()
    user = ListView.user.groups.values('name')
    context = {
        'list':list_,
        'user':user ,
    }
    return render (ListView,'Lists/classes.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','datahandler'])
def ManageContentListView(ListView):
    user = ListView.user.groups.values('name')
    session = get_object_or_404(Session , session_number = '1')
    if ListView.method == 'POST':
        list_ = []
        if ListView.POST.get('date'):
            for i in Content.objects.all():
                if str(i.class_name.pk) == str(ListView.POST.get('class')):
                    if str(ListView.POST.get('date')) == str(str(session.session_start_date + timedelta(days=i.day-1))):
                        list_.append(i)
        if ListView.POST.get('subject'):
            for i in Content.objects.all():
                if str(i.class_name.pk) == str(ListView.POST.get('class')):
                    if str(ListView.POST.get('subject')) == str(i.subject.pk):
                        list_.append(i)
        classes = Classes.objects.all()
        subjects = Subjects.objects.all()
        context = {
            'list':list_,
            'user':user ,
            'classes':classes ,
            'subjects':subjects ,
        }
        return render (ListView,'Lists/content.html',context)
    else:
        list_ = Content.objects.all()
        classes = Classes.objects.all()
        subjects = Subjects.objects.all()
        context = {
            'list':list_,
            'user':user ,
            'classes':classes ,
            'subjects':subjects ,
        }
        return render (ListView,'Lists/content.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def ManageSubjectListView(ListView):
    list_ = Subjects.objects.all()
    user = ListView.user.groups.values('name')
    context = {
        'list':list_,
        'user':user ,
    }
    return render (ListView,'Lists/subjects.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def ManageModuleListView(ListView):
    list_ = Module.objects.all()
    user = ListView.user.groups.values('name')
    context = {
        'list':list_,
        'user':user ,
    }
    return render (ListView,'Lists/module.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def ManageClassSubjectsListView(ListView):
    list_ = ClassSubjects.objects.all()
    user = ListView.user.groups.values('name')
    context = {
        'list':list_,
        'user':user ,
    }
    return render (ListView,'Lists/classsubjects.html',context)

