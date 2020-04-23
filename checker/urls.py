from django.urls import path
from . import checkerviews

urlpatterns = [
    path('',checkerviews.ManageCheckerProfileView, name='checker_profile'),
    path('class/<pk>',checkerviews.ManageCheckerClassView, name='full_class'),
    path('class/check/<pk>/<id>',checkerviews.ManageCheckerCheckView, name='student_copy_check'),
]