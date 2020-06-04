from django.shortcuts import render , redirect , get_object_or_404
from .models import *
from .forms import *
from authentication.forms import *
import random
from django.contrib.auth.models import Group

def ManageIndivisualsListView(ListView , pk = None):
    user = ListView.user.groups.values('name')
    if pk:
        indivisual = []
        for i in Indivisuals.objects.all():
            if i.school:
                if str(i.school.pk) == pk:
                    indivisual.append(i)
    else:
        indivisual = Indivisuals.objects.all()
    school = School.objects.all()
    context = {
        'school' : school ,
        'user' : user ,
        'indivisual' : indivisual ,
    }
    return render(ListView , 'Indivisuals/list.html' , context)

def ManageIndivisualsCreateView(CreateView , pk=None):
    user = CreateView.user.groups.values('name')
    if pk:
        school = get_object_or_404(School , pk = pk)
    else:
        school = 'No'
    if CreateView.method == 'POST':
        data = CreateView.POST
        username = ""
        for i in data.get('name'):
            if str(i) != ' ':
                username = str(username) + str(i.lower())
        for i in data.get('father_name'):
            if str(i) != ' ':
                username = str(username) + str(i.lower())
        p = ['a','b','c','d','e','1','2','3','4','5']
        random.shuffle(p)
        pas = ''
        for i in range(0,4):
            pas = pas + p[i]
        password = '{}@123'.format(pas)
        user_form = CreateUserForm({
            'username' : username ,
            'email' : '{}@gmail.com'.format(username) ,
            'password1' : password ,
            'password2' : password ,
        })
        user_form.save()
        user = User.objects.get(username = username)
        group = Group.objects.get(name='Individuals')
        user.groups.add(group)
        form = IndivisualsForm({
            'user' : user.pk ,
            'name' : data.get('name') ,
            'father_name' : data.get('father_name') ,
            'school' : data.get('school') ,
            'mobile' : data.get('mobile') ,
            'clas' : data.get('clas') ,
            'fees' : data.get('fees') ,
            'password' : password ,
            'active' : data.get('active') ,
        })
        form.save()
        return redirect('indivisuals_list')
    else:
        form = IndivisualsForm()
        context = {
            'school' : school ,
            'user' : user ,
            'form' : form ,
        }
        return render(CreateView , 'Indivisuals/Create/create.html' , context)

def ManageIndivisualsDetailView(DetailView , pk):
    user = DetailView.user.groups.values('name')
    indivisual = get_object_or_404(Indivisuals , pk = pk)
    context = {
        'user' : user ,
        'indivisual' : indivisual ,
    }
    return render(DetailView , 'Indivisuals/detail.html' , context)

def ManageIndivisualsEditView(EditView , pk):
    user = EditView.user.groups.values('name')
    indivisual = get_object_or_404(Indivisuals , pk = pk)
    if EditView.method == 'POST':
        data = EditView.POST
        form = IndivisualsForm({
            'user' : indivisual.user ,
            'name' : data.get('name') ,
            'father_name' : data.get('father_name') ,
            'school' : data.get('school') ,
            'mobile' : data.get('mobile') ,
            'clas' : data.get('clas') ,
            'fees' : data.get('fees') ,
            'password' : indivisual.password ,
            'active' : data.get('active') ,
        }or None , instance = indivisual)
        form.save()
        return redirect('indivisuals_detail',indivisual.pk)
    else:
        form = IndivisualsForm(instance = indivisual)
        context = {
            'user' : user ,
            'form' : form ,
        }
        return render(EditView , 'Indivisuals/edit.html' , context)
    
def ManageIndivisualsDeleteView(DeleteView , pk):
    indivisual = get_object_or_404(Indivisuals , pk = pk)
    user = indivisual.user
    user.delete()
    indivisual.delete()
    return redirect('indivisuals_list')

