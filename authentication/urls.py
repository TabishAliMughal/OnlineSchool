from django.urls import path
from . import views


urlpatterns = [
	path('register/ask', views.AskRegister, name="register_ask"),
	path('register/school', views.RegisterSchool, name="register_as_school"),
	path('register/pairent', views.RegisterPairent, name="register_as_pairent"),
	path('register/visitor', views.RegisterVisitor, name="register_as_visitor"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
]