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
    context = {
        'checker': checker ,
        'user': user ,
        'class' : classes ,
    }
    return render(ProfileView,'Checker/Profile.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Checker'])
def ManageCheckerClassView(ClassView,pk,id):
    user = ClassView.user.groups.values('name')
    checker = ClassView.user
    classes = get_object_or_404(CheckerClass , pk = id)
    students = []
    for i in ClassSubjects.objects.all():
        if str(i.class_name) == str(classes.subject.class_name) and str(i.subject_name) == str(classes.subject.subject_name):
            for s in TeacherClassStudents.objects.all():
                if str(s.clas.clas) == str(classes.subject.class_name):
                    status = ''
                    count = '0'
                    checked = '0'
                    exam_checker = ''
                    for a in ExamAnswers.objects.all():
                        if s.pk == a.student.pk:
                            if str(a.exam.subject) == str(classes.subject.subject_name):
                                count = int(count) + 1
                                if str(a.checked) == 'True':
                                    checked = int(checked) + 1
                                    if count == checked:
                                        status = 'Checked'
                                if str(a.checked) == 'False':
                                        exam_checker = a.checker
                                elif str(a.checked) == 'Pending':
                                    checked = int(checked) + 1
                                    if count == checked:
                                        status = 'Pending'
                                        exam_checker = a.checker
                                elif str(a.checked) == 'Claimed':
                                    checked = int(checked) + 1
                                    if count == checked:
                                        status = 'Claimed'
                                        exam_checker = a.checker
                    numbers = '0'
                    for x in QuestionsChecked.objects.all():
                        if str(x.student.pk) == str(s.pk):
                            if str(x.question.exam.subject) == str(classes.subject.subject_name):
                                numbers = int(numbers) + x.obtained
                                exam_checker = x.checker
                    students.append({'pk':s.pk,'name':s.name,'count':count,'status':status,'numbers':numbers,'checker':exam_checker})
    context = {
        'class' : classes ,
        'checker' : checker ,
        'user': user ,
        'students':students,
    }
    return render(ClassView,'Checker/Class.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Checker'])
def ManageCheckerClassCreateView(CreateView,pk):
    user = CreateView.user.groups.values('name')
    checker = CreateView.user
    if CreateView.method == 'POST':
        subject = CreateView.POST.get('subject')
        for i in CheckerClass.objects.all():
            if str(i.subject.pk) != str(subject) and str(i.checker.pk) != str(checker.pk):
                form = ManageCheckerClassCreateForm({
                    'checker': checker.pk ,
                    'subject': subject ,
                })
                form.save()
        return redirect('checker_profile')
    else:
        form = ManageCheckerClassCreateForm()
        context = {
            'form': form ,
            'user': user ,
        }
        return render(CreateView,'Checker/ClassCreate.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Checker'])
def ManageCheckerCheckView(CheckView,student,checker,clas):
    user = CheckView.user.groups.values('name')
    checker = CheckView.user.pk
    student = get_object_or_404(TeacherClassStudents , pk = student)
    checker_class = get_object_or_404(CheckerClass , pk = clas)
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
                        if str(ea.exam.subject) == str(checker_class.subject.subject_name):
                            if str(ea.checked) == 'False' or str(ea.checked) == 'Pending' or str(ea.checked) == 'Claimed':
                                ans_form = ManageExamAnswersForm({
                                    'student' : ea.student ,
                                    'exam' : ea.exam ,
                                    'picture' : ea.picture ,
                                    'checker' : checker ,
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
        return redirect('full_class',id,clas)
    else:
        marks = '0'
        file = []
        questions = []
        answers = []
        mar = []
        for d in ExamQuestions.objects.all():
            if str(student.clas.clas) == str(d.exam.class_name):
                if str(d.exam.subject.pk) == str(checker_class.subject.subject_name.pk):
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
            if str(i.student.pk) == str(student.pk):
                if str(i.exam.subject) == str(checker_class.subject.subject_name):
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
                            if str(x.student.pk) == str(student.pk):
                                if str(checker) == str(x.checker.pk):
                                    if str(x.question.exam.subject) == str(checker_class.subject.subject_name):
                                        a = str(i.picture)
                                        answers.append(a[7:])
                                        mar.append(x.obtained)
                        m = '0'
                        for v in ExamQuestions.objects.all():
                            if str(student.clas.clas) == str(i.exam.class_name):
                                if str(v.exam.subject) == str(checker_class.subject.subject_name):
                                    questions.append({
                                        'pk' : v.pk ,
                                        'exam' : v.exam ,
                                        'file' : v.file ,
                                        'question' : v.question ,
                                        'marks' : v.marks ,
                                        'mar' : mar[int(m)] ,
                                        'che': 'recheck' ,
                                    })
                                    marks = int(marks) + int(v.marks)
                                    v = str(v.file)
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
                    elif str(i.checked) == 'Claimed' :
                        marks = '0'
                        file = []
                        questions = []
                        for x in QuestionsChecked.objects.all():
                            if str(x.student.pk) == str(student.pk):
                                if str(checker) == str(x.checker.pk):
                                    if str(x.question.exam.subject) == str(checker_class.subject.subject_name):
                                        a = str(i.picture)
                                        answers.append(a[7:])
                                        mar.append(x.obtained)
                        m = '0'
                        for v in ExamQuestions.objects.all():
                            if str(student.clas.clas) == str(i.exam.class_name):
                                if str(v.exam.subject) == str(checker_class.subject.subject_name):
                                    questions.append({
                                        'pk' : v.pk ,
                                        'exam' : v.exam ,
                                        'file' : v.file ,
                                        'question' : v.question ,
                                        'marks' : v.marks ,
                                        'mar' : mar[int(m)] ,
                                        'che': 'recheck' ,
                                    })
                                    marks = int(marks) + int(v.marks)
                                    v = str(v.file)
                                    file.append(v[7:])
                                    m = int(m) + 1
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

@login_required(login_url='login')
@allowed_users(allowed_roles=['Teacher'])
def ManageCheckerStudentCopyCheckClaimView(ClaimView,exam,student):
    user = ClaimView.user.groups.values('name')
    exam = get_object_or_404(ExamStatus , pk = exam)
    student = get_object_or_404(TeacherClassStudents , pk = student)
    for i in ExamAnswers.objects.all():
        if str(i.student.pk) == str(student.pk):
            if str(i.exam.pk) == str(exam.pk):
                ans_form = ManageExamAnswersForm({
                            'student' : i.student ,
                            'exam' : i.exam ,
                            'picture' : i.picture ,
                            'checker' : i.checker ,
                            'checked' : 'Claimed' ,
                        } or None , instance = i)
                ans_form.save()
    return redirect('student_profile',student.pk)
