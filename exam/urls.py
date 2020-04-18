from django.urls import path
from . import views

urlpatterns = [
    path('class/students/exam/<id>/',views.ManageClassExamView, name='teacher_class_exam'),
    path('class/students/exam/print/questions/<id>/',views.ManageClassExamQuestionPrintView, name='exam_print_questions'),
    path('class/students/exam/print/file/<id>/',views.ManageClassExamFilePrintView, name='exam_print_file'),
    path('class/student/exam/upload/picture/<id>/<pk>/',views.ManageAddStudentExamPictureView, name='exam_upload_pictures'),
]