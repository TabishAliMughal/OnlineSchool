from django.shortcuts import render , get_list_or_404 , get_object_or_404 , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group , User
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only
from teacher.models import *
from .models import *
from exam.models import *



@login_required(login_url='login')
@allowed_users(allowed_roles=['Parent'])
def ManageProfileView(ProfileView):
    user = ProfileView.user.groups.values('name')
    loged = ProfileView.user
    student = []
    all_students = []
    for i in TeacherClassStudents.objects.all():
        all_students.append(i)
    for i in StudentPairent.objects.all():
        for v in all_students:
            if str(i.parent) == str(loged):
                if str(i.student) not in str(student):
                    student.append(i.student)
    context = {
        'student': student ,
        'user': user ,
    }
    return render(ProfileView,'Parents/Profile.html',context)
