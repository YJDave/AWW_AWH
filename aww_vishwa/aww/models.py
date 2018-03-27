from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# FIXME: Change this to choice fields, dictionary, list
# from modal.
class State(models.Model):
	name = models.CharField(max_length=250)

	def __str__(self):
		return self.name

class District(models.Model):
	state = models.ForeignKey(State)
	name = models.CharField(max_length=250)

	def __str__(self):
		return self.name

class Project(models.Model):
	state = models.ForeignKey(State)
	discrict = models.ForeignKey(District)
	name = models.CharField(max_length=250)

	def __str__(self):
		return self.name

class Center(models.Model):
	state = models.ForeignKey(State)
	discrict = models.ForeignKey(District)
	project = models.ForeignKey(Project)
	sector = models.PositiveIntegerField(default=0, blank=True)
	pincode = models.PositiveIntegerField(default=0, blank=True)
	name = models.CharField(max_length=250)
	address = models.CharField(max_length=1000, default="")
	logitude = models.PositiveIntegerField(default=0, blank=True)
	latitude = models.PositiveIntegerField(default=0, blank=True)

	def __str__(self):
		return self.name

class Admin(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	center = models.ForeignKey(Center)
	def __str__(self):
		return self.name

class Subscribers(models.Model):
	phone_no = PhoneNumberField()
	def __str__(self):
		return str(self.phone_no)

class Vacancy(models.Model):
	center = models.ForeignKey(Center)
	created_date = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return str(self.center)

class Application(models.Model):
	center = models.ForeignKey(Center)
	POSITION_CHOICES = (
		('w', "worker"),
		('h', "helper"),
	)
	for_position = models.CharField(max_length=1, choices=POSITION_CHOICES, default='w')
	name = models.CharField(max_length=250)
	phone_no = PhoneNumberField()
	GRADUATION_CHOICES = (
		('2', '7 pass'),
		('3', '10 pass'),
		('4', '12 pass'),
		('5', 'graduate'),
	)
	graduation = models.CharField(max_length=1, choices=GRADUATION_CHOICES, default='D')
	is_married = models.BooleanField(default=True)
	village = models.CharField(max_length=300)
	area = models.CharField(max_length=300)
	ward = models.CharField(max_length=300)
	pincode = models.PositiveIntegerField(default=0)
	has_birth_certificate = models.BooleanField(default=False)
	has_marriage_certificate = models.BooleanField(default=False)
	has_ration_card = models.BooleanField(default=False)
	has_adhaar_card = models.BooleanField(default=False)
	digital_mark = models.PositiveIntegerField(default=0)
	is_selected = models.BooleanField(default=False)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.digital_mark = int(self.graduation)
		if (self.has_birth_certificate):
			self.digital_mark += 2
		if (self.has_marriage_certificate):
			self.digital_mark += 2
		if (self.has_ration_card):
			self.digital_mark += 2
		if (self.has_adhaar_card):
			self.digital_mark += 2
		if (not self.is_married):
			self.digital_mark = 0
		super(Application, self).save(*args, **kwargs)

