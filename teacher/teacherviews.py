from django.shortcuts import render , get_list_or_404 , get_object_or_404 , redirect , HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group , User
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only
from .models import *
from .forms import *
from content.models import *
from exam.models import *


@login_required(login_url='login')
@allowed_users(allowed_roles=['Teacher'])
def ManageTeacherProfileView(ProfileView):
    exam = []
    classes = []
    user = ProfileView.user.groups.values('name')
    teacher = ProfileView.user
    for i in TeacherClass.objects.all():
        if str(i.teacher) == str(teacher):
            classes.append(i)
    for i in ExamStatus.objects.all():
        for v in classes:
            if str(i.class_name.pk) == str(v.clas.pk):
                if str(i.status) == 'True':
                    exam.append(i)
                else:
                    exam = ['No Active Exams']
            else:
                exam = ['No Active Exams']
    context = {
        'exam': exam ,
        'user': user ,
        'class' : classes ,
    }
    return render(ProfileView,'Teacher/Profile.html',context)

def ManageTeacherClassView(ListView,id):
    exam = []
    clas = []
    classes = []
    user = ListView.user.groups.values('name')
    tea = ListView.user
    teacher = get_object_or_404(TeacherClass , pk = id)
    for i in TeacherClass.objects.all():
        if str(i.teacher) == str(tea):
            classes.append(i)
    for i in TeacherClassStudents.objects.all():
        if str(i.clas.pk) == str(id):
            clas.append(i)
    for i in ExamStatus.objects.all():
        for v in classes:
            if str(i.class_name.pk) == str(v.clas.pk):
                if str(i.status) == 'True':
                    exam.append(i)
                else:
                    exam = ['No Active Exams']
            else:
                exam = ['No Active Exams']
    context = {
        'exam': exam ,
        'teacher': teacher ,
        'user': user ,
        'class' : clas ,
    }
    return render(ListView,'Teacher/Display/Class.html',context)

def ManageAddStudentView(CreateView,id):
    if CreateView.method == 'POST':
        clas = id
        name = CreateView.POST.get('name')
        father = CreateView.POST.get('father_name')
        contact = CreateView.POST.get('contact')
        address = CreateView.POST.get('address')
        picture = CreateView.POST.get('picture')
        if str(picture) == '':
            picture = 'null'
        form = TeacherClassStudentCreateForm({
            'clas' : clas ,
            'name' : name ,
            'father_name' : father ,
            'contact' : contact ,
            'address' : address ,
            'picture' : picture ,
        })
        form.save()
        return redirect('teacher_class',id)
    else:
        clas = get_object_or_404(TeacherClass,pk = id)
        user = CreateView.user.groups.values('name')
        limit = ''
        form = TeacherClassStudentCreateForm()
        if str(TeacherClassStudents.objects.count()) >= str(clas.limit):
            limit = 'Reached'
        context = {
            'limit': limit ,
            'class': clas ,
            'form': form ,
            'user': user ,
        }
        return render(CreateView,'Teacher/Create/Student.html',context)

def ManageEditStudentView(EditView,id,pk):
    student = get_object_or_404(TeacherClassStudents, pk = pk)
    if EditView.method == 'POST':
        clas = id
        name = EditView.POST.get('name')
        father = EditView.POST.get('father_name')
        contact = EditView.POST.get('contact')
        address = EditView.POST.get('address')
        picture = EditView.POST.get('picture')
        if str(picture) == '':
            picture = 'null'
        form = TeacherClassStudentCreateForm({
            'clas' : clas ,
            'name' : name ,
            'father_name' : father ,
            'contact' : contact ,
            'address' : address ,
            'picture' : picture ,
        }or None , instance=student)
        # form = TeacherClassStudentCreateForm(EditView.POST)
        # print(form)
        form.save()
        return redirect('teacher_class',id)
    else:
        clas = get_object_or_404(TeacherClass,pk = id)
        user = EditView.user.groups.values('name')
        form = TeacherClassStudentCreateForm(instance=student)
        context = {
            'class': clas ,
            'form': form ,
            'user': user ,
        }
        return render(EditView,'Teacher/Edit/Student.html',context)

def ManageDeleteStudentView(DeleteView,id,pk):
    TeacherClassStudents.objects.filter(pk = pk).delete()
    return redirect('teacher_class',id)


