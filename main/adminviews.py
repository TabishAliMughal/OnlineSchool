from django.shortcuts import render , get_object_or_404 , get_list_or_404 , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group , User
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only
from teacher.models import *
from checker.models import *
from indivisuals.models import *


@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def ManageProfilesView(ProfileView):
    user = ProfileView.user.groups.values('name')
    checkers = Group.objects.get(name="Checker")
    checkers = checkers.user_set.all()
    teachers = Group.objects.get(name="Teacher")
    teachers = teachers.user_set.all()
    individualuser = Group.objects.get(name="Individuals")
    individualuser = individualuser.user_set.all()
    k = int('0')
    for i in Indivisuals.objects.all():
        if i.school == None :
            k = k + 1
    schools = []
    for s in School.objects.all():
        f = int('0')
        for i in Indivisuals.objects.all():
            if i.school != None:
                if str(s.pk) == str(i.school.pk):
                    f = f + 1
        schools.append({'school':s,'students':f})
    students = []
    for i in TeacherClass.objects.all():
        stud = int('0')
        for stu in TeacherClassStudents.objects.all():
            if str(i.pk) == str(stu.clas.pk):
                stud = stud + 1
        students.append({'teacher':i.teacher,'students':stud})
        
    context = {
        'students': students ,
        'individuals': k ,
        'schoolstudents': schools,
        'checkers': checkers ,
        'teachers': teachers ,
        'user': user ,
    }
    return render(ProfileView,'Admin/Profiles.html',context)
