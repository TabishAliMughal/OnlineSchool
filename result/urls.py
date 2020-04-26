from django.urls import path
from . import resultviews

urlpatterns = [
    path(r'teacher/class/student/result/\d12345<id>910\d/\d12345<pk>910\d',resultviews.ManageTeacherClassStudentResultView, name='teacher_class_student_result'),
    path(r'teacher/class/student/result/\d12345<id>910\d/',resultviews.ManageTeacherClassResultView, name='teacher_class_result'),

]