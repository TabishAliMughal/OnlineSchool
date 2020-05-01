from django.urls import path
from . import studentviews

urlpatterns = [
    path(r'profile/\d12345<id>910\d/',studentviews.ManageProfileView, name='student_profile'),
]