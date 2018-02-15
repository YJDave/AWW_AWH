from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import (
	UserSignupForm,
	AppSignupForm,
)
from .models import (
	AppUser,
)

# Create your views here.

login_url = "/signup/"

def home(request):
	return render(request, "home.html", {})

def signupForm(request):
	if request.method == 'POST':
		userform = UserSignupForm(request.POST)
		appform = AppSignupForm(request.POST)
		if userform.is_valid() and appform.is_valid():
			return signupUser(request)
	else:
		userform = UserSignupForm()
		appform = AppSignupForm()
	return render(request, "signup.html", {'userform': userform, 'appform': appform})

def signupUser(request):
	userform = UserSignupForm(request.POST)
	appform = AppSignupForm(request.POST)
	user = userform.save(commit=True)
	appuser = appform.save(commit=False)
	appuser.user = user
	appuser.save()
	# This is hash password(encoded password)
	raw_password = userform.cleaned_data.get('password1')
	user = authenticate(username=user.username, password=raw_password)
	login(request, user)
	return redirect("/accounts/profile/")

@login_required(login_url=login_url)
def userAccount(request):
	appUser = get_object_or_404(AppUser, user=request.user)
	return render(request, "account.html", {})
