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
    user = EditView.user.groups.values('name')
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
            'user':user ,
        }
        return render(EditView , 'Forms/Edit/classes.html' , context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def ManageSubjectEditView(EditView,pk):
    user = EditView.user.groups.values('name')
    data = get_object_or_404(Subjects, pk = pk)
    if EditView.method == 'POST':
        form = SubjectsForm(EditView.POST or None, instance=data)
        if form.is_valid:
            form.save()
            return redirect('subject')
    else:
        form = SubjectsForm(instance=data)
        context = {
            'user':user ,
            'form' : form,
        }
        return render(EditView ,'Forms/Edit/subjects.html' , context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def ManageClassSubjectsEditView(EditView,pk):
    user = EditView.user.groups.values('name')
    data = get_object_or_404(ClassSubjects, pk = pk)
    if EditView.method == 'POST':
        form = ClassSubjectsForm(EditView.POST or None, instance=data)
        if form.is_valid:
            form.save()
            return redirect('class_subject')
    else:
        form = ClassSubjectsForm(instance=data)
        context = {
            'user':user ,
            'form' : form,
        }
        return render(EditView ,'Forms/Edit/classsubjects.html' , context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def ManageModuleEditView(EditView,pk):
    user = EditView.user.groups.values('name')
    data = get_object_or_404(Module, pk = pk)
    if EditView.method == 'POST':
        form = ModuleForm(EditView.POST or None, instance=data)
        if form.is_valid:
            form.save()
            return redirect('module')
    else:
        form = ModuleForm(instance=data)
        context = {
            'user':user ,
            'form' : form,
        }
        return render(EditView ,'Forms/Edit/module.html' , context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def ManageContentEditView(EditView,pk):
    user = EditView.user.groups.values('name')
    data = get_object_or_404(Content, pk = pk)
    videos = []
    k = int('0')
    for i in Videos.objects.all():
        if str(i.content.pk) == str(data.pk):
            videos.append(i)
            k = k + 1
    images = []
    l = int('0')
    for i in Images.objects.all():
        if str(i.content.pk) == str(data.pk):
            images.append(i)
            l = l + 1
    if EditView.method == 'POST':
        vid = EditView.POST
        form = ContentForm(EditView.POST or None, instance=data)
        if form.is_valid:
            form.save()
            url = vid.getlist('url')
            p = int('0')
            for i in url:
                p = p+1
            v = int('0')
            for i in videos:
                i.delete()
            for i in url:
                form2 = VideoForm({
                    'content' : data.pk ,
                    'url' : url[v]
                })
                v = v + 1
                form2.save()
            img = []
            image = EditView.FILES.getlist('image')
            preimage = EditView.POST.getlist('pre-image')
            for i in image:
                img.append(i)
            p = int('0')
            for i in images:
                for v in preimage:
                    if str(v) != str(i.pk):
                        i.delete()
            for i in img:
                form2 = ImageForm({
                    'content' : data.pk ,},{
                    'image' : img[p]
                })
                p = p + 1
                form2.save()
            return redirect('content')
    else:
        form = ContentForm(instance=data)
        date = str(data.date)
        context = {
            'date' : date ,
            'user':user ,
            'form' : form ,
            'videos' : videos ,
            'images' : images ,
        }
        return render(EditView ,'Forms/Edit/content.html' , context)
