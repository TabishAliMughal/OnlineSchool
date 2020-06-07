from django.shortcuts import render , redirect , get_object_or_404 , get_list_or_404
from requirments.models import *
from .models import *
from teacher.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only


@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','Teacher'])
def ManageDateSelectView(SelectView):
    user = SelectView.user.groups.values('name')
    if SelectView.method == 'POST':
        Date = SelectView.POST.get('date')
        return redirect('class_select',Date)
    context = {
        'user':user ,
    }
    return render(SelectView , 'Select/date.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','Teacher'])
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

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','Teacher'])
def ManageSubjectSelectView(SelectView,date,Ccode):
    user = SelectView.user.groups.values('name')
    list_ = []
    FClassSubjects = []
    if SelectView.user.is_authenticated:
        for i in user:
            if str(i.get('name')) == 'Teacher':
                for v in Content.objects.all():
                    if str(v.date) == str(date) and str(v.class_name.pk) == str(Ccode):
                        if str(v.therefor) == 'O':
                            list_.append(v)
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
    context = {
        'user':user ,
        'date' : FDate,
        'class' : FClass,
        'class_subjects' : FClassSubjects,
    }
    return render(SelectView , 'Select/subject.html' , context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','Teacher'])
def ManageContentSelectView(SelectView,date,Ccode,subject):
    cont = []
    sub = get_object_or_404(Subjects , subject_name = subject)
    con = Content.objects.all()
    user = SelectView.user.groups.values('name')
    for rows in con:
        Cc = get_object_or_404(Classes, class_name = rows.class_name)
        if str(Cc.code) == str(Ccode):
            if str(rows.subject) == str(sub):
                if str(rows.date) == str(date):
                    if str(rows.therefor) == 'O':
                        FContent = get_list_or_404(Content , date = date , class_name = Ccode , subject = sub)
                        cont.append(FContent)
    context = {'user':user ,'content' : cont,}
    return render(SelectView , 'Select/content_select.html' , context)

def ManageContentView(ContentView, code):
    Contents = get_object_or_404(Content,code = code)
    user = ContentView.user.groups.values('name')
    videos = []
    for i in Videos.objects.all():
        if str(i.content.pk) == str(Contents.pk):
            videos.append(i)
    images = []
    for i in Images.objects.all():
        if str(i.content.pk) == str(Contents.pk):
            images.append(i)
    print(images)
    context = {
        'user':user ,
        'content' : Contents ,
        'videos' : videos ,
        'images' : images ,
    }
    return render(ContentView , 'Select/content.html' , context)