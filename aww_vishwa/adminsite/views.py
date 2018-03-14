from django.shortcuts import render
from django.contrib.auth import views

def AdminHomePage(request):
	return render(request, "admin/home.html", {})

def ListCenters(request):
	return render(request, "admin/centers.html", {})

def CenterInfo(request, center_id):
	return render(request, "admin/center.html", {})

def CenterApplications(request, center_id):
	return render(request, "admin/applications.html", {})

def ApplicationInfo(request, center_id, application_id):
	return render(request, "admin/application.html", {})
