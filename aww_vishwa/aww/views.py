from django.shortcuts import render
from django.contrib.auth import views
from .forms import (
	SubscribeUserForm,
	ApplyForm,
)
from .models import Center

def HomePage(request):
	return render(request, "aww/home.html", {})

def SubscribeUser(request):
	if request.method == 'POST':
		form = SubscribeUserForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = SubscribeUserForm()
	return render(request, "aww/subscribe.html", {'form': SubscribeUserForm})

def ListCirculars(request):
	return render(request, "aww/circulars.html", {})

def ListVacancies(request):
	# centerName = Center.name
	# sectorName = Center.sector
	# stateList = Center.state
	# districtList = Center.district
	# projectList = Center.project
	# workerVacancies = Center.W_vacancies
	# helperVacancies = Center.H_vacancies

	# return render(request, "aww/vacancies.html", {'centerName':centerName, 
	# 'sectorName':sectorName, 'stateList':stateList,'districtList':districtList,
	# 'projectList':projectList,'workerVacancies':workerVacancies, 
	# 'helperVacancies':helperVacancies})
	return render(request, "aww/vacancies.html", {})

def ApplyForVacancy(request):
	if request.method == 'POST':
		form = ApplyForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = ApplyForm()
	return render(request, "aww/apply.html", {"form": form})

def ListVacancyResults(request):
	return render(request, "aww/results.html", {})

def VacancyResult(request, result_id):
	
	return render(request, "aww/result.html", {})

def ListEligibility(request):
	return render(request, "aww/eligibility.html", {})

def ListLearningMaterials(request):
	return render(request, "aww/learning-materials.html", {})

def Guidelines(request):
	return render(request, "aww/guidelines.html", {})

def Schemes(request):
	return render(request,"aww/schemes.html",{})

def ContactUs(request):
	return render(request,"aww/contact-us.html",{})
