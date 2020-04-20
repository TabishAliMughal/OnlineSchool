from django.urls import path
from . import views

urlpatterns = [
    path(r'class/students/exam/\d12345<id>910\d/',views.ManageClassExamView, name='teacher_class_exam'),
    path(r'class/students/exam/print/questions/\d12345<id>910\d/',views.ManageClassExamQuestionPrintView, name='exam_print_questions'),
    path(r'class/students/exam/print/file/\d12345<id>910\d/',views.ManageClassExamFilePrintView, name='exam_print_file'),
    path(r'class/student/exam/upload/picture/\d12345<id>910\d/\d12345<pk>910\d/',views.ManageAddStudentExamPictureView, name='exam_upload_pictures'),
]