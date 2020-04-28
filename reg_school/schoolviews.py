from django.shortcuts import render , get_object_or_404 , get_list_or_404 , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group , User
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only
from teacher.models import *
from checker.models import *
from .forms import *


@login_required(login_url='login')
@allowed_users(allowed_roles=['School'])
def ManageSchoolProfileView(ProfileView):
    group = Group.objects.all()
    for i in group:
        if str(i) == 'Teacher':
            group = i
    user = ProfileView.user.groups.values('name')
    log_school = ProfileView.user
    s = School.objects.all()
    school = []
    teachers = []
    v = TeacherClass.objects.all()
    for i in v:
        if str(i.school) != 'None':
            if str(i.school.user.pk) == str(log_school.pk):
                teachers.append(i)
    for i in s:
        if str(i.user.pk) == str(log_school.pk):
            school.append(i)
    if school == []:
        school = 'No'
    context = {
        'group' : group ,
        'school': school ,
        'teachers': teachers ,
        'user': user ,
    }
    return render(ProfileView,'School/Profile.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['School'])
def ManageTeacherProfileDatailView(DetailView , id):
    user = DetailView.user.groups.values('name')
    asked = get_object_or_404(User,pk = id)
    students = '0'
    clas = []
    classes = []
    teachers = Group.objects.get(name="Teacher")
    teachers = teachers.user_set.all()
    for t in teachers:
        if str(t.pk) == str(asked.pk):
            for i in TeacherClass.objects.all():
                if str(i.teacher.pk) == str(id):
                    classes.append(i.clas)
            for i in TeacherClassStudents.objects.all():
                if str(i.clas.teacher.pk) == str(id):
                    clas.append(i.name)
            for i in clas:
                students = int(students) + 1
            context = {
                'classes' : classes ,
                'students' : students ,
                'user': user ,
                'teacher' : asked
            }
            return render(DetailView,'Teacher/ProfileDetail.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['School'])
def ManageSchoolCreateView(CreateView):
    user = CreateView.user.groups.values('name')
    if CreateView.method == "POST":
        rawdata = CreateView.POST
        school = rawdata.get('school')
        address = rawdata.get('address')
        form = ManageSchoolCreateForm({
            'school': school ,
            'address': address ,
            'user': CreateView.user.pk
        })
        form.save()
        return redirect('school_profile')
    else:
        form = ManageSchoolCreateForm()
        context = {
            'form' : form ,
            'user': user ,
        }
        return render(CreateView,'School/Create/School.html',context)