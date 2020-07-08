from django.shortcuts import render , redirect , get_object_or_404 , get_list_or_404
from requirments.models import *
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def ManageClassDeleteView(DeleteView,pk):
    data = Classes.objects.filter(pk = pk).delete()
    return redirect('class')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def ManageSubjectDeleteView(DeleteView,pk):
    data = Subjects.objects.filter(pk = pk).delete()
    return redirect('subject')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def ManageClassSubjectsDeleteView(DeleteView,pk):
    data = ClassSubjects.objects.filter(pk = pk).delete()
    return redirect('class_subject')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def ManageModuleDeleteView(DeleteView,pk):
    data = Module.objects.filter(pk = pk).delete()
    return redirect('module')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def ManageContentDeleteView(DeleteView,pk):
    data = Content.objects.filter(pk = pk).delete()
    return redirect('content')

def ManageContentPictureDeleteView(DeleteView,pk):
    data = get_object_or_404(Images , pk = pk)
    content = data.content.pk
    data.delete()
    return redirect('content_edit',content)
