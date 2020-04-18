from django.shortcuts import render , get_object_or_404 , get_list_or_404 , redirect ,HttpResponse
from .models import *
from static.renderer import PdfMaker
from .forms import *


def ManageClassExamView(ExamView,id):
    user = ExamView.user.groups.values('name')
    exam = get_object_or_404(ExamStatus,pk = id)
    questions = get_list_or_404(ExamQuestions , exam = id)
    context = {
        'questions' : questions ,
        'exam' : exam ,
        'user': user ,
    }
    return render(ExamView,'Exam/Exam.html',context)

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

def ManageClassExamFilePrintView(ExamView,id):
    file = get_object_or_404(ExamQuestions , exam = id)
    print(file.file)
    path = file.file
    return HttpResponse(path , 'application/pdf')


def ManageAddStudentExamPictureView(UploadView,id,pk):
    tea = UploadView.user
    classes = []
    exam = []
    for i in TeacherClass.objects.all():
        if str(i.teacher) == str(tea):
            classes.append(i)
    for i in ExamStatus.objects.all():
        for v in classes:
            if str(i.class_name.pk) == str(v.clas.pk):
                if str(i.status) == 'True':
                    exam.append(i.pk)
                else:
                    exam = ['No Active Exams']
            else:
                exam = ['No Active Exams']
    user = UploadView.user.groups.values('name')
    if UploadView.method == 'POST':
        form = ManageExamAnswersForm(UploadView.POST)
        for i in exam:
            exampk = i
        pic = UploadView.POST.get('pic')
        form  = ManageExamAnswersForm({
            'student' : int(pk) ,
            'exam' : int(exampk) ,
            'picture' : pic ,
        })
        # form.save()
        context = {
            'user': user ,
            'form' : 'Can not Save Data'
        }
        return render(UploadView,'Exam/PapersUpload.html',context)
    else:
        student = get_object_or_404(TeacherClassStudents, pk = pk)
        form = ManageExamAnswersForm()
        context = {
            'form': 'Can not Save Data' ,
            'student': student ,
            'user': user ,
        }
        return render(UploadView,'Exam/PapersUpload.html',context)