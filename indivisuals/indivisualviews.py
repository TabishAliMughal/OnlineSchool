from django.shortcuts import render , redirect , get_object_or_404
from .models import *
from .forms import *
from authentication.forms import *
import random
from django.contrib.auth.models import User , Group
from content.models import *
import datetime
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group , User
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only



@login_required(login_url='login')
@allowed_users(allowed_roles=['Individuals'])
def ManageIndivisualProfileView(ProfileView , pk = None):
    user = ProfileView.user.groups.values('name')
    individual = []
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
            if str(str(individual.session.session_start_date + timedelta(days=i.day-1))) == str(datetime.date.today()):
                if pk:
                    if str(i.pk) == str(pk):
                        videos = []
                        images = []
                        for vid in Videos.objects.all():
                            if str(i.pk) == str(vid.content.pk):
                                videos.append(vid)
                        content.append({'content':i,'period':v,'videos':videos })
                else:
                    content.append({'content':i,'period':v})
                    v = v + 1
    g = str(individual.clas)
    if g == str('Prep I') or g == str('Prep I') or g == str('Prep II'):
        v = 'pre'
    elif g == str('First') or g == str('Second') or g == str('Third') or g == str('Fourth') or g == str('Fifth') or g == str('Sixth') or g == str('Seventh') or g == str('Eighth'):
        v = 'primary'
    elif g == str('Ninth'):
        v = 'ninth'
    elif g == str('Tenth'):
        v = 'tenth'
    context = {
        'user':user,
        'content':content,
        'clas':v,
        'individual':individual,
    }
    if pk:
        return render(ProfileView,'Indivisuals/Period.html',context)
    else:
        day = datetime.datetime.now().strftime("%A")
        if str(day) == 'Saturday' or str(day) == 'Sunday' :
            return render(ProfileView,'Indivisuals/Weekend.html',context)
        elif str(datetime.date.today()) <= str(individual.session.session_start_date - timedelta(days=1)):
            return render(ProfileView,'Indivisuals/BeforeStart.html',context)
        elif str(individual.active) == str('False'):
            return render(ProfileView,'Indivisuals/FeeNotSubmited.html',context)            
        else:
            return render(ProfileView,'Indivisuals/Profile.html',context)

def ManageIndivisualDocumentsView(DocumentView , pk):
    user = DocumentView.user.groups.values('name')
    content = get_object_or_404(Content , pk = int(pk))
    images = []
    for img in Images.objects.all():
        if str(img.content.pk) == str(content.pk):
            images.append(img)
    context = {
        'user':user,
        'content':content,
        'images':images,
    }
    return render(DocumentView,'Indivisuals/Documents.html',context)
