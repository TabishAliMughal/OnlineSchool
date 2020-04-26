from django.shortcuts import render , redirect , get_object_or_404 , get_list_or_404
from requirments.models import *
from .models import *
from teacher.models import *

def ManageDateSelectView(SelectView):
    user = SelectView.user.groups.values('name')
    if SelectView.method == 'POST':
        Date = SelectView.POST.get('date')
        return redirect('class_select',Date)
    context = {
        'user':user ,
    }
    return render(SelectView , 'Select/date.html',context)

def ManageClassSelectView(SelectView,date):
    user = SelectView.user.groups.values('name')
    teacher = []
    if SelectView.user.is_authenticated:
        for i in user:
            if str(i.get('name')) == 'Teacher':
                teacher = SelectView.user
                for i in TeacherClass.objects.all():
                    if str(i.teacher) == str(teacher.pk):
                        teacher.append(i)
                return redirect('subject_select',date,teacher.clas.pk)
    FDate = date
    FClass = Classes.objects.all()
    context = {
        'user':user ,
        'date' : FDate,
        'class' : FClass,
    }
    return render(SelectView , 'Select/class.html' , context)

def ManageSubjectSelectView(SelectView,date,Ccode):
    user = SelectView.user.groups.values('name')
    list_ = []
    FClassSubjects = []
    if SelectView.user.is_authenticated:
        for i in user:
            if str(i.get('name')) == 'Teacher':
                for i in Content.objects.all():
                    if str(i.date) == str(date) and str(i.class_name) == str(Ccode):
                        list_.append(i)
                # list_ = get_list_or_404(Content , date = date , class_name = Ccode )
                context = {
                    'list':list_,
                    'user':user ,
                }
                return render (SelectView,'Lists/content.html',context)
    FDate = date
    FClass = get_object_or_404(Classes, code = Ccode)
    for i in ClassSubjects.objects.all():
        if str(i.class_name.pk) == str(Ccode):
            FClassSubjects.append(i)
    # FClassSubjects = get_list_or_404(ClassSubjects , class_name = Ccode)
    context = {
        'user':user ,
        'date' : FDate,
        'class' : FClass,
        'class_subjects' : FClassSubjects,
    }
    return render(SelectView , 'Select/subject.html' , context)

def ManageContentSelectView(SelectView,date,Ccode,subject):
    cont = []
    for rows in Subjects.objects.all():
        sub = get_object_or_404(Subjects , subject_name = subject)
    con = Content.objects.all()
    user = SelectView.user.groups.values('name')
    for rows in con:
        Cc = get_object_or_404(Classes, class_name = rows.class_name)
        if str(Cc.code) == str(Ccode):
            if rows.subject == sub:
                if str(rows.date) == str(date):
                    FContent = get_list_or_404(Content , date = date , class_name = Ccode , subject = sub)
                    cont.append(FContent)
    context = {'user':user ,'content' : cont,}
    return render(SelectView , 'Select/content_select.html' , context)

def ManageContentView(ContentView, code):
    Contents = get_object_or_404(Content,code = code)
    user = ContentView.user.groups.values('name')
    context = {
        'user':user ,
        'content' : Contents,
    }
    return render(ContentView , 'Select/content.html' , context)