from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import (
	Subscribers,
	Application,
)

class SubscribeUserForm(forms.ModelForm):
	class Meta:
		model = Subscribers
		fields = ("phone_no",)

# class ApplyForm(forms.ModelForm):
# 	class Meta:
# 		model = Application
# 		fields = ('phone_no')
