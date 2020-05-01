from django.urls import path
from . import parentviews

urlpatterns = [
    path('',parentviews.ManageProfileView, name='parent_profile'),
    # path(r'detail/\d12345<id>910\d/',parentviews.ManageStudentProfileView, name='parent_profile_detail'),
]