from django.urls import path
from . import adminviews

urlpatterns = [
    path('',adminviews.ManageProfilesView, name='profiles'),
    path(r'teacher/detail/\d12345<id>910\d',adminviews.ManageProfilesDatailView, name='profile_detail'),
]