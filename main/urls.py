from django.urls import path
from . import adminviews

urlpatterns = [
    path('',adminviews.ManageProfilesView, name='profiles'),
    path('teacher/detail/<id>',adminviews.ManageProfilesDatailView, name='profile_detail'),
]