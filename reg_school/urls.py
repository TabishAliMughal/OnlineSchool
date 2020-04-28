from django.urls import path
from . import schoolviews

urlpatterns = [
    path('',schoolviews.ManageSchoolProfileView, name='school_profile'),
    path('create/',schoolviews.ManageSchoolCreateView, name='school_create'),
    path(r'teacher/detail/\d12345<id>910\d',schoolviews.ManageTeacherProfileDatailView, name='teacher_profile_detail'),
]