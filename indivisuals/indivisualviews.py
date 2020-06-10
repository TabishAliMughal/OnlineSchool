from django.shortcuts import render , redirect , get_object_or_404
from .models import *
from .forms import *
from authentication.forms import *
import random
from django.contrib.auth.models import User , Group
from content.models import *
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group , User
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only



@login_required(login_url='login')
@allowed_users(allowed_roles=['Individuals'])
def ManageIndivisualProfileView(ProfileView , pk = None):
    user = ProfileView.user.groups.values('name')
    for i in user:
        if str(i.get('name')) == 'Individuals':
            curuser = ProfileView.user
    for i in Indivisuals.objects.all():
        if str(i.user.pk) == str(curuser.pk):
            individual = i
    content = []
    v = int('1')
    for i in Content.objects.all():
        if str(i.class_name.pk) == str(individual.clas.pk):
            if str(datetime.date.today()) == str(i.date):
                if pk:
                    if str(i.pk) == str(pk):
                        videos = []
                        images = []
                        for vid in Videos.objects.all():
                            if str(i.pk) == str(vid.content.pk):
                                videos.append(vid)
                        for img in Images.objects.all():
                            if str(img.content.pk) == str(i.pk):
                                images.append(img)
                        content.append({'content':i,'period':v,'videos':videos , 'images':images})
                        print(images)
                else:
                    content.append({'content':i,'period':v})
                v = v + 1
    context = {
        'user':user,
        'content':content,
    }
    if pk:
        return render(ProfileView,'Indivisuals/Period.html',context)
    else:
        if str(datetime.date.today()) <= str('2020-07-06'):
            return render(ProfileView,'Indivisuals/BeforeStart.html',context)
        elif str(individual.active) == str('False'):
            return render(ProfileView,'Indivisuals/FeeNotSubmited.html',context)            
        else:
            return render(ProfileView,'Indivisuals/Profile.html',context)
