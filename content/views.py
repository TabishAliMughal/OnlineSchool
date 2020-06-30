from django.shortcuts import render , redirect , get_object_or_404 , get_list_or_404
from requirments.models import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only
from teacher.models import *
from .forms import *

def ManageMainView(SelectView):
    user = SelectView.user.groups.values('name')
    v = '1'
    tea = []
    for i in TeacherClass.objects.all():
        loc = []
        map = i.location
        for m in map:
            loc.append(m)
        tea.append({'num':int(v),'teacher':i,'lat':loc[1],'lon':loc[0]})
        v = int(v) + 1
    context = {
        'locator':tea ,
        'user':user ,
    }
    for i in user:
        if str(i.get('name')) == 'Teacher':
            return redirect('teacher_profile')
        elif str(i.get('name')) == 'Admin':
            return redirect('profiles')
        elif str(i.get('name')) == 'Checker':
            return redirect('checker_profile')
        elif str(i.get('name')) == 'School':
            return redirect('school_profile')
        elif str(i.get('name')) == 'Parent':
            return redirect('parent_profile')
        elif str(i.get('name')) == 'Student':
            return redirect('student_profile',SelectView.user.pk)
        elif str(i.get('name')) == 'Individuals':
            return redirect('indivisual_profile')
    return render(SelectView , 'Main.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def ManageSelectToAddView(SelectView):
    user = SelectView.user.groups.values('name')
    context = {
        'user':user ,
    }
    return render(SelectView , 'MainSelect.html' , context)


def ManageAllView(SelectView):
    user = SelectView.user.groups.values('name')
    context = {
        'user':user ,
    }
    return render(SelectView , 'All.html' , context)


def ManageDemoView(DemoView):
    user = DemoView.user.groups.values('name')
    f = []
    for i in range(6,13):
        f.append(i)
    k = []
    for i in range(13,20):
        k.append(i)
    context = {
        'date1': f ,
        'date2': k ,
        'user': user ,
    }
    return render(DemoView , 'Demo.html' , context)

def ManageDemoListView(ListView,date):
    user = ListView.user.groups.values('name')
    v = '0'
    for i in date:
        v = int(v) + 1
    if str(v) == '1':
        date = str("2020-07-0{}".format(date))
    elif str(v) == '2':
        date = str("2020-07-{}".format(date))
    content = []
    for v in Classes.objects.all():
        k = int('0')
        abc = []
        for i in Content.objects.all():
            if str(v.pk) == str(i.class_name.pk):
                if str(i.date) == str(date):
                    k = k + 1
                    abc.append({
                        'period' : k ,
                        'pk': i.pk ,
                        'class_name' : i.class_name ,
                        'subject' : i.subject ,
                        'module' : i.module ,
                    })
        content.append({'class':v , 'content' : abc})
    context = {
        'date' : date ,
        'content' : content,
        'user': user ,
    }
    return render(ListView , 'Lists/DemoContent.html' , context)
