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

class ApplyForm(forms.ModelForm):
	class Meta:
		model = Application
		fields = ("center", "for_position", "name", "phone_no", "graduation", "is_married", "village",
			     "area", "ward", "pincode", "has_birth_certificate", "has_marriage_certificate", "has_ration_card",
			     "has_adhaar_card")

