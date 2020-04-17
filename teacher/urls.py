from django.urls import path
from . import teacherviews

urlpatterns = [
    # View
    path('',teacherviews.ManageTeacherProfileView, name='teacher_profile'),
    path('class/students/<id>/',teacherviews.ManageTeacherClassView, name='teacher_class'),
    # Student
    path('class/student/add/<id>/',teacherviews.ManageAddStudentView, name ='add_student'),
    path('class/student/edit/<id>/<pk>',teacherviews.ManageEditStudentView, name ='edit_student'),
    path('class/student/delete/<id>/<pk>',teacherviews.ManageDeleteStudentView, name ='delete_student'),
]