from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .user_handeling import unauthenticated_user, allowed_users, admin_only
from .forms import *

@unauthenticated_user
def AskRegister(request):
    return render(request , 'Authentication/RegisterAsk.html')

@unauthenticated_user
def RegisterSchool(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			group = Group.objects.get(name='School')
			user.groups.add(group)
			messages.success(request, 'Account was created for ' + username)
			return redirect('login')
	context = {
        'form':form
        }
	return render(request, 'Authentication/RegisterSchool.html', context)
	
@unauthenticated_user
def RegisterPairent(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			group = Group.objects.get(name='Pairents')
			user.groups.add(group)
			messages.success(request, 'Account was created for ' + username)
			return redirect('login')
	context = {
        'form':form
        }
	return render(request, 'Authentication/RegisterPairent.html', context)
	
@unauthenticated_user
def RegisterVisitor(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			group = Group.objects.get(name='Visitor')
			user.groups.add(group)
			messages.success(request, 'Account was created for ' + username)
			return redirect('login')
	context = {
        'form':form
        }
	return render(request, 'Authentication/RegisterVisitor.html', context)

@unauthenticated_user
def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('main')
		else:
			messages.info(request, 'Username OR password is incorrect')
	context = {}
	return render(request, 'Authentication/LoginPage.html', context)

def logoutUser(request):
	logout(request)
	return redirect('main')

# @admin_only
# @login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])