from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Admin(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

class Center(models.Model):
	name = models.CharField(max_length=250)
	address = models.CharField(max_length=1000, default="", blank=True)
	admins = models.ForeignKey(Admin, on_delete=models.CASCADE)

class Subscribers(models.Model):
	phone_no = PhoneNumberField()

class Vacancy(models.Model):
	center = models.OneToOneField(Center)
	created_date = models.DateTimeField(auto_now_add=True)

class Application(models.Model):
	center = models.OneToOneField(Center)
	POSITION_CHOICES = (
		('w', "worker"),
		('h', "heler"),
	)
	for_position = models.CharField(max_length=1, choices=POSITION_CHOICES, default='w')
	name = models.CharField(max_length=250)
	phone_no = PhoneNumberField()
	GRADUATION_CHOICES = (
		('D', '7 pass'),
		('C', '10 pass'),
		('B', '12 pass'),
		('A', 'graduate'),
	)
	graduation = models.CharField(max_length=1, choices=GRADUATION_CHOICES, default='D')
	is_married = models.BooleanField(default=True)
	village = models.CharField(max_length=300)
	area = models.CharField(max_length=300)
	ward = models.CharField(max_length=300)
	pincode = models.PositiveIntegerField(default=0)
	has_birth_certi = models.BooleanField(default=False)
	has_marriage_certi = models.BooleanField(default=False)
	has_rashon_certi = models.BooleanField(default=False)
	has_adhaar_certi = models.BooleanField(default=False)
	has_waters_certi = models.BooleanField(default=False)
