from django.shortcuts import render , redirect , get_object_or_404 , get_list_or_404
from requirments.models import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only

def ManageMainView(SelectView):
    user = SelectView.user.groups.values('name')
    context = {
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