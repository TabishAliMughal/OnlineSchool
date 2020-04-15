from django.shortcuts import render , redirect , get_object_or_404 , get_list_or_404
from requirments.models import *
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only


@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def ManageClassEditView(EditView,pk):
    data = get_object_or_404(Classes, pk = pk)
    if EditView.method == 'POST':
        form = ClassesForm(EditView.POST or None, instance=data)
        if form.is_valid:
            form.save()
            return redirect('class')
    else:
        form = ClassesForm(instance=data)
        context = {
            'form' : form,
        }
        return render(EditView , 'Forms/Edit/classes.html' , context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def ManageSubjectEditView(EditView,pk):
    data = get_object_or_404(Subjects, pk = pk)
    if EditView.method == 'POST':
        form = SubjectsForm(EditView.POST or None, instance=data)
        if form.is_valid:
            form.save()
            return redirect('subject')
    else:
        form = SubjectsForm(instance=data)
        context = {
            'form' : form,
        }
        return render(EditView ,'Forms/Edit/subjects.html' , context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def ManageClassSubjectsEditView(EditView,pk):
    data = get_object_or_404(ClassSubjects, pk = pk)
    if EditView.method == 'POST':
        form = ClassSubjectsForm(EditView.POST or None, instance=data)
        if form.is_valid:
            form.save()
            return redirect('class_subject')
    else:
        form = ClassSubjectsForm(instance=data)
        context = {
            'form' : form,
        }
        return render(EditView ,'Forms/Edit/classsubjects.html' , context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def ManageModuleEditView(EditView,pk):
    data = get_object_or_404(Module, pk = pk)
    if EditView.method == 'POST':
        form = ModuleForm(EditView.POST or None, instance=data)
        if form.is_valid:
            form.save()
            return redirect('module')
    else:
        form = ModuleForm(instance=data)
        context = {
            'form' : form,
        }
        return render(EditView ,'Forms/Edit/module.html' , context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def ManageContentEditView(EditView,pk):
    data = get_object_or_404(Content, pk = pk)
    if EditView.method == 'POST':
        form = ContentForm(EditView.POST or None, instance=data)
        if form.is_valid:
            form.save()
            return redirect('content')
    else:
        form = ContentForm(instance=data)
        context = {
            'form' : form,
        }
        return render(EditView ,'Forms/Edit/content.html' , context)
