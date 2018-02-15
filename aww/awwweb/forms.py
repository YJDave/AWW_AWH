from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import (
	AppUser,
)

class UserSignupForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

class AppSignupForm(forms.ModelForm):
	class Meta:
		model = AppUser
		fields = ('first_name', 'last_name', 'legal_name', 'address', 'phone_no',
			      'degree_group', 'achievements', 'age')
