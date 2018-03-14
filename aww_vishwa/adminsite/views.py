from django.shortcuts import render
from django.contrib.auth import views

class AdminHomePage(views.TemplateView):
	template_name = "admin/home.html"
	pass;

class ListCenters(views.TemplateView):
	template_name = "admin/centers.html"
	pass;

class CenterInfo(views.TemplateView):
	template_name = "admin/center.html"
	pass;

class CenterApplications(views.TemplateView):
	template_name = "admin/applications.html"
	pass;
