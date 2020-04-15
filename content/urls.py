from django.urls import path
from . import views
from . import selectviews
from . import formviews
from . import listviews
from . import editviews
from . import deleteviews

urlpatterns = [
    # Main
    path('',views.ManageMainView, name ='main'),
    path('view/',views.ManageAllView, name ='all'),
    path('select/add',views.ManageSelectToAddView, name ='select_to_add'),

    # Create
    path('class/create/',formviews.ManageClassesCreateView, name ='class_form'),
    path('module/create/',formviews.ManageModuleCreateView, name ='module_form'),
    path('content/create/',formviews.ManageContentCreateView, name ='content_form'),
    path('subject/create/',formviews.ManageSubjectsCreateView, name ='subject_form'),
    path('classsubject/create/',formviews.ManageClassSubjectsCreateView, name ='class_subject_form'),
    
    # List
    path('class/list/',listviews.ManageClassListView, name ='class'),
    path('content/list/',listviews.ManageContentListView, name ='content'),
    path('subject/list/',listviews.ManageSubjectListView, name ='subject'),
    path('module/list/',listviews.ManageModuleListView, name ='module'),
    path('classsubject/list/',listviews.ManageClassSubjectsListView, name ='class_subject'),

    # Edit
    path('class/edit/<pk>/',editviews.ManageClassEditView, name ='class_edit'),
    path('content/edit/<pk>/',editviews.ManageContentEditView, name ='content_edit'),
    path('subject/edit/<pk>/',editviews.ManageSubjectEditView, name ='subject_edit'),
    path('module/edit/<pk>/',editviews.ManageModuleEditView, name ='module_edit'),
    path('classsubject/edit/<pk>/',editviews.ManageClassSubjectsEditView, name ='class_subject_edit'),

    # Delete
    path('class/delete/<pk>/',deleteviews.ManageClassDeleteView, name ='class_delete'),
    path('content/delete/<pk>/',deleteviews.ManageContentDeleteView, name ='content_delete'),
    path('subject/delete/<pk>/',deleteviews.ManageSubjectDeleteView, name ='subject_delete'),
    path('module/delete/<pk>/',deleteviews.ManageModuleDeleteView, name ='module_delete'),
    path('classsubject/delete/<pk>/',deleteviews.ManageClassSubjectsDeleteView, name ='class_subject_delete'),

    # Select
    path('date/',selectviews.ManageDateSelectView, name ='date_select'),
    path('<date>/',selectviews.ManageClassSelectView, name ='class_select'),
    path('content/<code>/',selectviews.ManageContentView, name ='content'),
    path('<date>/<Ccode>/',selectviews.ManageSubjectSelectView, name ='subject_select'),
    path('<date>/<Ccode>/<subject>/',selectviews.ManageContentSelectView, name ='content_select'),

]
