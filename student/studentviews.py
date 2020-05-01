from django.shortcuts import render , get_object_or_404 , get_list_or_404 , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group , User
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only
from teacher.models import *
from exam.models import *
from .models import *

@login_required(login_url='login')
@allowed_users(allowed_roles=['Student','Parent','Teacher'])
def ManageProfileView(ProfileView,id):
    user = ProfileView.user.groups.values('name')
    for i in Student.objects.all():
        if str(ProfileView.user.pk) == str(i.profile.pk) :
            student = get_object_or_404(TeacherClassStudents , pk = i.student.pk)
        else:
            student = get_object_or_404(TeacherClassStudents , pk = id)
    exam = []
    abc = []
    for i in ExamStatus.objects.all():
        if str(i.class_name.pk) == str(student.clas.pk):
            if str(i.status) == 'True':
                abc.append(i)
    if abc != []:
        for e in abc:
            answers = '0'
            for i in ExamAnswers.objects.all():
                if str(i.student.pk) == str(student.pk):
                    if str(e.subject) == str(i.exam.subject):
                        answers = int(answers) + 1
                        status = i.checked
            exam.append({'exam' : e, 'answers' : answers , 'status' : status })
    if exam == []:
        exam = 'No Active Exams'
    context = {
        'student': student ,
        'exam': exam ,
        'user': user ,
    }
    return render(ProfileView,'Student/Profile.html',context)

