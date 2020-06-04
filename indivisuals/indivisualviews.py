from django.shortcuts import render , redirect , get_object_or_404
from .models import *
from .forms import *
from authentication.forms import *
import random
from django.contrib.auth.models import User , Group
from content.models import *
import datetime

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
                        for vid in Videos.objects.all():
                            if str(i.pk) == str(vid.content.pk):
                                videos.append(vid)
                        content.append({'content':i,'period':v,'videos':videos})
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
        return render(ProfileView,'Indivisuals/Profile.html',context)
