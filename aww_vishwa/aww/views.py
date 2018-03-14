from django.shortcuts import render
from django.contrib.auth import views

class HomePage(views.TemplateView):
	template_name = "aww/home.html"
	pass;
