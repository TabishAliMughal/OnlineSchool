from django.shortcuts import render , get_list_or_404 , get_object_or_404 , redirect , HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group , User
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only
from .models import *
from exam.forms import *
from .forms import *
from content.models import *
from exam.models import *
import webbrowser as wb
from .urls import *



@login_required(login_url='login')
@allowed_users(allowed_roles=['Checker'])
def ManageCheckerProfileView(ProfileView):
    user = ProfileView.user.groups.values('name')
    checker = ProfileView.user
    classes = []
    for i in CheckerClass.objects.all():
        if str(i.checker) == str(checker):
            classes.append(i)
    print(classes)
    context = {
        'user': user ,
        'class' : classes ,
    }
    return render(ProfileView,'Checker/Profile.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Checker'])
def ManageCheckerClassView(ClassView,pk):
    user = ClassView.user.groups.values('name')
    checker = ClassView.user
    classes = []
    for i in CheckerClass.objects.all():
        if str(checker.pk) == str(pk):
            if str(i.checker) == str(checker):
                classes.append(i.subject)
    students = []
    for i in ClassSubjects.objects.all():
        for c in classes:
            if str(i.class_name) == str(c.class_name) and str(i.subject_name) == str(c.subject_name):
                for s in TeacherClassStudents.objects.all():
                    if str(s.clas.clas) == str(c.class_name):
                        status = ''
                        count = '0'
                        checked = '0'
                        for a in ExamAnswers.objects.all():
                            if s.pk == a.student.pk:
                                count = int(count) + 1
                                if str(a.checked) == 'True':
                                    checked = int(checked) + 1
                                    if count == checked:
                                        status = 'Checked'
                                elif str(a.checked) == 'Pending':
                                    checked = int(checked) + 1
                                    if count == checked:
                                        status = 'Pending'
                        numbers = '0'
                        for x in QuestionsChecked.objects.all():
                            if str(x.student.pk) == str(s.pk):
                                numbers = int(numbers) + x.obtained
                                exam_checker = x.checker
                        students.append({'pk':s.pk,'name':s.name,'count':count,'status':status,'numbers':numbers,'checker':exam_checker})
    context = {
        'checker': checker ,
        'abc' : pk ,
        'user': user ,
        'students':students,
    }
    return render(ClassView,'Checker/Class.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Checker'])
def ManageCheckerCheckView(CheckView,pk,id):
    user = CheckView.user.groups.values('name')
    checker = CheckView.user.pk
    student = get_object_or_404(TeacherClassStudents , pk = pk)
    if CheckView.method == 'POST':
        rawdata = CheckView.POST
        v = '0'
        c = '0'
        check = CheckView.POST.get('d')
        for i in rawdata:
            if str(v) >= '2':
                question = get_object_or_404(ExamQuestions , pk = i)
                marks = CheckView.POST.get(i)
                if str(check) == 'recheck':
                    for v in QuestionsChecked.objects.all():
                        if str(checker) == str(v.checker.pk) and str(question.pk) == str(v.question.pk) and str(student.pk) == str(v.student.pk):
                            c = int(c)+1
                            form = ManageCheckingSaveForm({
                                'checker' : checker ,
                                'question' : question.pk ,
                                'student' : student ,
                                'obtained' : marks ,
                            } or None , instance = v)
                            form.save()
                else:
                    form = ManageCheckingSaveForm({
                        'checker' : checker ,
                        'question' : question.pk ,
                        'student' : student ,
                        'obtained' : marks ,
                    })
                    form.save()
                for ea in ExamAnswers.objects.all():
                    if str(ea.student.pk) == str(student.pk):
                        if str(ea.checked) == 'False' or str(ea.checked) == 'Pending':
                            ans_form = ManageExamAnswersForm({
                                'student' : ea.student ,
                                'exam' : ea.exam ,
                                'picture' : ea.picture ,
                                'checked' : 'True' ,
                            } or None , instance = ea)
                            ans_form.save()
            else:
                v = int(v) + 1
        for i in CheckedCount.objects.all():
            if str(i.student.pk) == str(pk):
                pass
            else:
                form = ManageCheckerCountForm({
                    'checker' : checker ,
                    'student' : pk ,
                    'exam' : i.exam ,
                    'count' : int('1') ,
                })
                form.save()
        return redirect('full_class',id)
    else:
        marks = '0'
        file = []
        questions = []
        answers = []
        mar = []
        for d in ExamQuestions.objects.all():
            if str(student.clas.clas) == str(d.exam.class_name):
                questions.append({
                    'pk': d.pk ,
                    'exam' : d.exam ,
                    'file' : d.file ,
                    'question' : d.question ,
                    'marks' : d.marks ,
                })
                marks = int(marks) + int(d.marks)
                v = str(d.file)
                file.append(v[7:])
        for i in ExamAnswers.objects.all():
            if str(i.student.pk) == str(pk):
                if str(i.checked) == 'False' :
                    a = str(i.picture)
                    answers.append(a[7:])
                    ans_form = ManageExamAnswersForm({
                        'student' : i.student ,
                        'exam' : i.exam ,
                        'picture' : i.picture ,
                        'checker' : checker ,
                        'checked' : 'Pending' ,
                    } or None , instance = i)
                    ans_form.save()
                elif str(i.checked) == 'True':
                    marks = '0'
                    file = []
                    questions = []
                    for x in QuestionsChecked.objects.all():
                        if str(x.student.pk) == str(pk):
                            if str(checker) == str(x.checker.pk):
                                a = str(i.picture)
                                answers.append(a[7:])
                                mar.append(x.obtained)
                    m = '0'
                    for i in ExamQuestions.objects.all():
                        if str(student.clas.clas) == str(i.exam.class_name):
                            questions.append({
                                'pk' : i.pk ,
                                'exam' : i.exam ,
                                'file' : i.file ,
                                'question' : i.question ,
                                'marks' : i.marks ,
                                'mar' : mar[int(m)] ,
                                'che': 'recheck' ,
                            })
                            marks = int(marks) + int(i.marks)
                            v = str(i.file)
                            file.append(v[7:])
                            m = int(m) + 1
                elif str(i.checked) == 'Pending' :
                    if str(i.checker.pk) == str(checker):
                        a = str(i.picture)
                        answers.append(a[7:])
                        ans_form = ManageExamAnswersForm({
                            'student' : i.student ,
                            'exam' : i.exam ,
                            'picture' : i.picture ,
                            'checker' : checker ,
                            'checked' : 'Pending' ,
                        } or None , instance = i)
                        ans_form.save()
                    else:
                        answers = 'Copies Checking Already Pending'
        if answers == []:
            answers = 'No Answers'
        context = {
            'mar' : mar ,
            'student' : student,
            'file' : file,
            'answers' :answers,
            'marks' : marks ,
            'questions' : questions ,
            'user': user ,
        }
        return render(CheckView,'Checker/CopyCheck.html',context)

