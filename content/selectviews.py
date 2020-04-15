from django.shortcuts import render , redirect , get_object_or_404 , get_list_or_404
from requirments.models import *
from .models import *

def ManageDateSelectView(SelectView):
    if SelectView.method == 'POST':
        Date = SelectView.POST.get('date')
        return redirect('class_select',Date)
    return render(SelectView , 'Select/date.html')

def ManageClassSelectView(SelectView,date):
    FDate = date
    FClass = Classes.objects.all()
    context = {
        'date' : FDate,
        'class' : FClass,
    }
    return render(SelectView , 'Select/class.html' , context)

def ManageSubjectSelectView(SelectView,date,Ccode):
    FDate = date
    FClass = get_object_or_404(Classes, code = Ccode)
    FClassSubjects = get_list_or_404(ClassSubjects , class_name = Ccode)
    context = {
        'date' : FDate,
        'class' : FClass,
        'class_subjects' : FClassSubjects,
    }
    return render(SelectView , 'Select/subject.html' , context)

def ManageContentSelectView(SelectView,date,Ccode,subject):
    for rows in Subjects.objects.all():
        sub = get_object_or_404(Subjects , subject_name = subject)
    con = Content.objects.all()
    for rows in con:
        # context = {'content' : 'No Module',}
        Cc = get_object_or_404(Classes, class_name = rows.class_name)
        if str(Cc.code) == str(Ccode):
            # context = {'content' : 'No Content',}
            if rows.subject == sub:
                # context = {'content' : 'No Content For Today',}
                if str(rows.date) == str(date):
                    FContent = get_list_or_404(Content , date = date , class_name = Ccode , subject = sub)
                    context = {'content' : FContent,}
    return render(SelectView , 'Select/content_select.html' , context)

def ManageContentView(ContentView, code):
    Contents = get_object_or_404(Content,code = code)
    context = {
        'content' : Contents,
    }
    return render(ContentView , 'Select/content.html' , context)