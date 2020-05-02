from django.urls import path
from . import adminviews

urlpatterns = [
    path('',adminviews.ManageProfilesView, name='profiles'),
]