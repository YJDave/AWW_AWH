from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Participant(models.Model):
	MIN_AGE = 18
	REQUIRED_PHONE_NO = False
	REQUIRED_ADDRESS = False
	EDUCATIONAL_DEGREE_CHOICES = (
		('AA', "B.E."),
		('AB', "B.Com."),
		('BB', "M.E."),
		('BC', "Graduate"),
	)

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	legal_name = models.CharField(max_length=400)
	address = models.CharField(max_length=1400, blank=REQUIRED_ADDRESS)
	phone_no = PhoneNumberField(blank=REQUIRED_PHONE_NO)
	age = models.PositiveIntegerField(validators=[MinValueValidator(MIN_AGE)])
	joined_date = models.DateTimeField(auto_now_add=True)
	degree_group = models.CharField(max_length=2, choices=EDUCATIONAL_DEGREE_CHOICES, default='BC')
	unemployed = models.BoolField(blank=True, default=False)

	def __str__(self):
		return str(self.user) + " : " + self.legal_name
