from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import LoginForm
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
import smtplib









def login_page(request):
	if request.method == 'POST':
		form = LoginForm(request.POST or None)
		if form.is_valid():
			username  = form.cleaned_data.get("username")
			password  = form.cleaned_data.get("password")
			user = authenticate(username=username, password=password)
			if user is not None:
			 	if user.is_active:
			 		login(request, user)
			 		return redirect('administrator:administrator')
			 	else:
			 		return HttpResponse('Disabled account')
			else:
				return HttpResponse('Invalid login')
	else:
		form = LoginForm()
	context = {"form": form}
	return render(request, "account/login.html", context)


def logout_page(request):
	logout(request)
	return redirect('account:logged_out')
	
def logged_out(request):
	return render(request, "account/logout.html", {})