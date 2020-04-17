from django.urls import path
from . import views


urlpatterns = [
	path('register/ask', views.AskRegister, name="register_ask"),
	path('register/<id>', views.Register, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
]