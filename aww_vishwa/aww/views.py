from django.shortcuts import render
from django.contrib.auth import views
from .forms import (
	SubscribeUserForm,
)

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
	return render(request, "aww/vacancies.html", {})

def ApplyForVacancy(request):
	return render(request, "aww/apply.html", {})

def ListVacancyResults(request):
	return render(request, "aww/results.html", {})

def VacancyResult(request, result_id):
	return render(request, "aww/result.html", {})

def ListEligibility(request):
	return render(request, "aww/eligibility.html", {})

def ListLearningMaterials(request):
	return render(request, "aww/learning-materials.html", {})
