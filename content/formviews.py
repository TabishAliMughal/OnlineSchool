from django.shortcuts import render , redirect , get_object_or_404 , get_list_or_404
from requirments.models import *
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only


@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def ManageClassesCreateView(CreateView):
    if CreateView.method == 'POST':
        form = ClassesForm(CreateView.POST)
        user = CreateView.user.groups.values('name')
        if form.is_valid:
            form.save()
            context = { 
                'user':user ,
                'return': 'Has Been Added SuccessFully'
            }
            return render(CreateView,'Forms/Created/classes.html',context)
        else:
            context = { 
                'user':user ,
                'return': 'Is Not Valid'
            }
            return render(CreateView,'Forms/Created/classes.html',context)
    else:
        form = ClassesForm()
        user = CreateView.user.groups.values('name')
        context = { 
            'user':user ,
            'form': form
        }
        return render(CreateView , 'Forms/Create/classes.html' , context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def ManageSubjectsCreateView(CreateView):
    user = CreateView.user.groups.values('name')
    if CreateView.method == 'POST':
        form = SubjectsForm(CreateView.POST)
        if form.is_valid:
            form.save()
            context = { 
                'user':user ,
                'user':user ,
                'return': 'Has Been Added SuccessFully'
            }
            return render(CreateView,'Forms/Created/subjects.html',context)
        else:
            context = { 
                'user':user ,
                'return': 'Is Not Valid'
            }
            return render(CreateView,'Forms/Created/subjects.html',context)
    else:
        form = SubjectsForm()
        context = { 
            'user':user ,
            'form': form
        }
        return render(CreateView ,'Forms/Create/subjects.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def ManageClassSubjectsCreateView(CreateView):
    user = CreateView.user.groups.values('name')
    if CreateView.method == 'POST':
        clas = CreateView.POST.get('class_name')
        subj = CreateView.POST.getlist('sub' , default='1')
        for i in subj:
            form = ClassSubjectsForm({
                'class_name' : clas ,
                'subject_name' : i ,
            })
            if form.is_valid:
                form.save()
        context = { 
            'user':user ,
            'return': 'Has Been Added SuccessFully'
        }
        return render(CreateView,'Forms/Created/classsubjects.html',context)
    else:
        form = ClassSubjectsForm()
        subject = Subjects.objects.all()
        context = { 
            'user':user ,
            'form': form ,
            'sub' : subject ,
        }
        return render(CreateView ,'Forms/Create/classsubjects.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def ManageModuleCreateView(CreateView):
    user = CreateView.user.groups.values('name')
    if CreateView.method == 'POST':
        form = ModuleForm(CreateView.POST)
        if form.is_valid:
            form.save()
            context = { 
                'user':user ,
                'return': 'Has Been Added SuccessFully'
            }
            return render(CreateView,'Forms/Created/module.html',context)
        else:
            context = { 
                'user':user ,
                'return': 'Is Not Valid'
            }
            return render(CreateView,'Forms/Created/module.html',context)
    else:
        form = ModuleForm()
        context = { 
            'user':user ,
            'form': form
        }
        return render(CreateView ,'Forms/Create/module.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def ManageContentCreateView(CreateView):
    user = CreateView.user.groups.values('name')
    if CreateView.method == 'POST':
        data = CreateView.POST
        form1 = ContentForm(CreateView.POST)
        k = ''
        if form1.is_valid:
            k = form1.save()
            url = data.getlist('url')
            v = int('0')
            for i in url:
                form2 = VideoForm({
                    'content' : k ,
                    'url' : url[v]
                })
                v = v + 1
                form2.save()
            image = CreateView.FILES.getlist('image')
            l = int('0')
            for v in image:
                form3 = ImageForm({
                    'content' : k ,
                },{
                    'image' : image[l] ,
                })
                l = l + 1
                form3.save()
            context = { 
                'user':user ,
                'return': 'Has Been Added SuccessFully'
            }
            return render(CreateView,'Forms/Created/content.html',context)
        else:
            context = { 
                'user':user ,
                'return': 'Is Not Valid'
            }
            return render(CreateView,'Forms/Created/content.html',context)
    else:
        form1 = ContentForm()
        form2 = VideoForm()
        form3 = ImageForm()
        context = { 
            'user':user ,
            'form1': form1,
            'form2': form2,
            'form3': form3,
        }
        return render(CreateView ,'Forms/Create/content.html', context)
