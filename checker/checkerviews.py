from django.shortcuts import render , get_list_or_404 , get_object_or_404 , redirect , HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group , User
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only
from .models import *
from .forms import *
from content.models import *
from exam.models import *
import webbrowser as wb
from .urls import *




@login_required(login_url='login')
@allowed_users(allowed_roles=['Checker'])
def ManageCheckerProfileView(ProfileView):
    user = ProfileView.user.groups.values('name')
    checker = ProfileView.user
    classes = []
    for i in CheckerClass.objects.all():
        if str(i.checker) == str(checker):
            classes.append(i)
    print(classes)
    context = {
        'user': user ,
        'class' : classes ,
    }
    return render(ProfileView,'Checker/Profile.html',context)


def ManageCheckerClassView(ClassView,pk):
    user = ClassView.user.groups.values('name')
    checker = ClassView.user
    classes = []
    for i in CheckerClass.objects.all():
        if str(checker.pk) == str(pk):
            if str(i.checker) == str(checker):
                classes.append(i.subject)
    students = []
    for i in ClassSubjects.objects.all():
        for c in classes:
            if str(i.class_name) == str(c.class_name) and str(i.subject_name) == str(c.subject_name):
                for s in TeacherClassStudents.objects.all():
                    if str(s.clas.clas) == str(c.class_name):
                        students.append(s)
    context = {
        'user': user ,
        'students':students,
    }
    return render(ClassView,'Checker/Class.html',context)

def ManageCheckerCheckView(CheckView,pk):
    if CheckView.method == 'POST':
        print(CheckView.POST)
    else:
        marks = '0'
        file = []
        questions = []
        answers = []
        user = CheckView.user.groups.values('name')
        student = get_object_or_404(TeacherClassStudents , pk = pk)
        for i in ExamQuestions.objects.all():
            if str(student.clas.clas) == str(i.exam.class_name):
                questions.append(i)
                marks = int(marks) + int(i.marks)
                v = str(i.file)
                print(v[7:])
                file.append(v[7:])
        for i in ExamAnswers.objects.all():
            if str(i.student.pk) == str(pk):
                a = str(i.picture)
                answers.append(a[7:])
        context = {
            'student' : student,
            'file' : file,
            'answers' :answers,
            'marks' : marks ,
            'questions' : questions ,
            'user': user ,
        }
        return render(CheckView,'Checker/CopyCheck.html',context)

def ManageCheckerCheckFileView(CheckView,pk):
    file = get_object_or_404(ExamQuestions , pk = pk)
    path = file.file
    return HttpResponse(path,'application/pdf')
