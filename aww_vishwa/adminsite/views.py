from django.shortcuts import render, get_object_or_404
from django.contrib.auth import views
from django.contrib.auth.decorators import login_required
from aww.models import (
	Application,
	Center,
	Admin,
)

login_url = "/login/"

@login_required(login_url=login_url)
def AdminHomePage(request):
	return render(request, "admin/home.html", {})

@login_required(login_url=login_url)
def ListCenters(request):
	user = get_object_or_404(Admin, user=request.user)
	user_project = user.project
	centers = Center.objects.filter(project=user_project)
	return render(request, "admin/centers.html", {"centers": centers})

@login_required(login_url=login_url)
def CenterInfo(request, center_id):
	center = get_object_or_404(Center, id=center_id)
	return render(request, "admin/center.html", {"center": center})

@login_required(login_url=login_url)
def CenterApplications(request, center_id):
	center = get_object_or_404(Center, id=center_id)
	applications = Application.objects.filter(center=center)
	return render(request, "admin/applications.html", {'applications': applications})

def ApplicationInfo(request, center_id, application_id):
	return render(request, "admin/application.html", {})
