from django.urls import path
from . import views
from . import indivisualviews

urlpatterns = [
    path(r'',views.ManageIndivisualsListView, name='indivisuals_list'),
    path(r'detail/<pk>',views.ManageIndivisualsDetailView, name='indivisuals_detail'),
    path(r'create',views.ManageIndivisualsCreateView, name='indivisuals_create'),
    path(r'edit/<pk>',views.ManageIndivisualsEditView, name='indivisuals_edit'),
    path(r'delete/<pk>',views.ManageIndivisualsDeleteView, name='indivisuals_delete'),

    # for school
    path(r'create/<pk>',views.ManageIndivisualsCreateView, name='indivisuals_create'),


    path(r'individual',indivisualviews.ManageIndivisualProfileView, name='indivisual_profile'),
    path(r'individual/content/<pk>',indivisualviews.ManageIndivisualProfileView, name='indivisual_content'),
]