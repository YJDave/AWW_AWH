from django.shortcuts import render
from django.contrib.auth import views

class AdminHomePage(views.TemplateView):
	template_name = "admin/home.html"
	pass;

