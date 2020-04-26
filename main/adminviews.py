from django.shortcuts import render , get_object_or_404 , get_list_or_404 , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group , User
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only
from teacher.models import *
from checker.models import *


@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def ManageProfilesView(ProfileView):
    user = ProfileView.user.groups.values('name')
    checkers = Group.objects.get(name="Checker")
    checkers = checkers.user_set.all()
    teachers = Group.objects.get(name="Teacher")
    teachers = teachers.user_set.all()
    context = {
        'checkers': checkers ,
        'teachers': teachers ,
        'user': user ,
    }
    return render(ProfileView,'Admin/Profiles.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def ManageProfilesDatailView(DetailView , id):
    user = DetailView.user.groups.values('name')
    asked = get_object_or_404(User,pk = id)
    students = '0'
    clas = []
    classes = []
    checkers = Group.objects.get(name="Checker")
    checkers = checkers.user_set.all()
    teachers = Group.objects.get(name="Teacher")
    teachers = teachers.user_set.all()
    for t in teachers:
        if str(t) == str(asked):
            for i in TeacherClass.objects.all():
                if str(i.teacher.pk) == str(id):
                    classes.append(i.clas)
            for i in TeacherClassStudents.objects.all():
                if str(i.clas.teacher.pk) == str(id):
                    clas.append(i.name)
            for i in clas:
                students = int(students) + 1
            context = {
                'classes' : classes ,
                'students' : students ,
                'user': user ,
                'teacher' : asked
            }
            return render(DetailView,'Teacher/ProfileDetail.html',context)
    for c in checkers:
        if str(c) == str(asked):
            for i in CheckerClass.objects.all():
                print(i.checker.pk)
                print(id)
                if str(i.checker.pk) == str(id):
                    classes.append(i.subject)
            for i in clas:
                students = int(students) + 1
            context = {
                'classes' : classes ,
                'user': user ,
                'teacher' : asked
            }
            return render(DetailView,'Checker/ProfileDetail.html',context)
