from django.shortcuts import render
from django.contrib.auth import views

class HomePage(views.TemplateView):
	template_name = "aww/home.html"
	pass;

class SubscribeUser(views.TemplateView):
	template_name = "aww/subscribe.html"
	pass;

class ListCirculars(views.TemplateView):
	template_name = "aww/circulars.html"
	pass;

class ListVacancies(views.TemplateView):
	template_name = "aww/vacancies.html"
	pass;

class ApplyForVacancy(views.TemplateView):
	template_name = "aww/apply.html"
	pass;

class ListVacancyResults(views.TemplateView):
	template_name = "aww/results.html"
	pass;

class VacancyResult(views.TemplateView):
	template_name = "aww/result.html"
	pass;

class ListEligibility(views.TemplateView):
	template_name = "aww/eligibility.html"
	pass;
