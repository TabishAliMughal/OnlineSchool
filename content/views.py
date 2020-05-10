from django.shortcuts import render , redirect , get_object_or_404 , get_list_or_404
from requirments.models import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only
from teacher.models import *

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
    for i in range(1,32):
        f.append(i)
    context = {
        'date': f ,
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
    for i in Content.objects.all():
        print(i.date)
        print(date)
        if str(i.date) == str(date):
            content.append(i)
    context = {
        'list' : content,
        'user': user ,
    }
    return render(ListView , 'Lists/content.html' , context)
