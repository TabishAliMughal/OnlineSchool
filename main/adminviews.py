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
