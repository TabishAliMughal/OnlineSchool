from django.shortcuts import render , get_object_or_404 , get_list_or_404 , redirect ,HttpResponse
from .models import *
from static.renderer import PdfMaker
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group , User
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only


@login_required(login_url='login')
@allowed_users(allowed_roles=['Teacher','Individuals'])
def ManageClassExamView(ExamView,id):
    user = ExamView.user.groups.values('name')
    exam = get_object_or_404(ExamStatus,pk = id)
    questions = get_list_or_404(ExamQuestions , exam = id)
    answers = int('0')
    for i in ExamAnswers.objects.all():
        if str(i.exam.pk) == str(exam.pk):
            if i.student.pk == (get_object_or_404(Indivisuals , user = ExamView.user)).pk:
                answers = answers + 1
    context = {
        'questions' : questions ,
        'exam' : exam ,
        'user': user ,
        'answers': answers ,
    }
    return render(ExamView,'Exam/Exam.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Teacher','Individuals'])
def ManageClassExamQuestionPrintView(PrintView,id):
    user = PrintView.user.groups.values('name')
    exam = get_object_or_404(ExamStatus,pk = id)
    questions = get_list_or_404(ExamQuestions , exam = id)
    context = {
        'questions' : questions ,
        'exam' : exam ,
        'user': user ,
    }
    pdf = PdfMaker('Exam/ExamQuestionsPrint.html', context)
    return HttpResponse(pdf, content_type='application/pdf')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Teacher','Individuals'])
def ManageClassExamFilePrintView(ExamView,id):
    file = get_object_or_404(ExamQuestions , exam = id)
    path = file.file
    return HttpResponse(path , 'application/pdf')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Teacher'])
def ManageTeacherClassExamAnswersStudentSelectView(SelectView,id,pk):
    exam = get_object_or_404(ExamStatus, pk = id)
    teacher = get_object_or_404(User , pk = pk)
    students = []
    classtud = []
    classes = []
    addedpics = []
    user = SelectView.user.groups.values('name')
    tea = SelectView.user
    for i in TeacherClass.objects.all():
        if str(i.teacher) == str(tea):
            if str(i.clas) == str(exam.class_name):
                classes.append(i)
    for c in classes:
        for i in TeacherClassStudents.objects.all():
            if str(i.clas.clas) == str(c.clas):
                classtud.append(i)
    for e in ExamAnswers.objects.all():
        for c in classtud:
            if str(e.student.pk) == str(c.pk) and str(e.exam.pk) == str(exam.pk) :
                addedpics.append(str(c.pk))
    for i in classtud:
        pics = addedpics.count(str(i.pk))
        students.append({
            'pk': i.pk ,
            'clas': i.clas ,
            'name': i.name ,
            'father_name': i.father_name ,
            'picsqty': pics ,
        })
    context = {
        'teacher': teacher ,
        'user': user ,
        'exam': exam ,
        'class' : students ,
    }
    return render(SelectView,'Exam/Class.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Teacher','Individuals'])
def ManageAddStudentExamPictureView(UploadView,id,pk=None):
    if pk:
        student = get_object_or_404(Indivisuals, pk = pk)
    else:
        student = get_object_or_404(Indivisuals , user = UploadView.user)
    selectedexam = get_object_or_404(ExamStatus , pk = id)
    user = UploadView.user.groups.values('name')
    form = ManageExamAnswersForm()
    tea = UploadView.user
    classes = []
    exam = []
    for i in TeacherClass.objects.all():
        if str(i.teacher) == str(tea):
            classes.append(i)
    if UploadView.method == 'POST':
        v = ExamAnswers.objects.count()
        filled_form  = ManageExamAnswersForm({
            'student' : student.pk ,
            'exam' : int(selectedexam.pk) ,
            'checked' : 'False' ,
        },UploadView.FILES)
        if filled_form.is_valid:
            filled_form.save()
        context = {
            'teacher': tea ,
            'student':student ,
            'exam': selectedexam ,
            'form' : form ,
            'student': student ,
            'user': user ,
        }
        return render(UploadView,'Exam/PapersUploaded.html',context)
    else:
        context = {
            'exam': selectedexam ,
            'form': form ,
            'student': student ,
            'user': user ,
        }
        return render(UploadView,'Exam/PapersUpload.html',context)

