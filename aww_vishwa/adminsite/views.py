from django.shortcuts import render
from django.contrib.auth import views
from aww.models import Application

def AdminHomePage(request):
	return render(request, "admin/home.html", {})

def ListCenters(request):
	return render(request, "admin/centers.html", {})

def CenterInfo(request, center_id):
	return render(request, "admin/center.html", {})

def CenterApplications(request, center_id):
	all_applications = Application.objects.all()
	return render(request, "admin/applications.html", {'applications': all_applications})

def ApplicationInfo(request, center_id, application_id):
	return render(request, "admin/application.html", {})
