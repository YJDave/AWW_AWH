from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# FIXME: Change this to choice fields, dictionary, list
# from modal.
# TODO: Write automated script to fill out states and districts on every new migrations
# Auto add all states, districts using automated script.
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
	sector = models.PositiveIntegerField()
	# TODO: Add validations in pincode field.
	pincode = models.PositiveIntegerField()
	# TODO: Name should be primary key or combination of sector and name should
	# be primary key.
	name = models.CharField(max_length=250)
	center_no = models.PositiveIntegerField()
	address = models.CharField(max_length=1000, default="")
	longitude = models.PositiveIntegerField(default=0, blank=True)
	latitude = models.PositiveIntegerField(default=0, blank=True)
	W_vacancies = models.PositiveIntegerField(default=0, blank=True)
	H_vacancies = models.PositiveIntegerField(default=0, blank=True)

	def __str__(self):
		return self.name

# FIXME: Improve admin model to map admin user to position.
class Admin(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	project = models.ForeignKey(Project)
	def __str__(self):
		return self.name

# Child Development Project Officer
class Admin_CDPO(models.Model):
	admin = models.ForeignKey(Admin)
	can_view = models.BooleanField(default=True)
	can_select_for_interview = models.BooleanField(default=True)
	can_select_for_position = models.BooleanField(default=False)
	can_fianlize_selection = models.BooleanField(default=False)

# Taluka Development officer
class Admin_TDO(models.Model):
	admin = models.ForeignKey(Admin)
	can_view = models.BooleanField(default=True)
	can_select_for_interview = models.BooleanField(default=True)
	can_select_for_position = models.BooleanField(default=False)
	can_fianlize_selection = models.BooleanField(default=False)

class Admin_DeputyCollector(models.Model):
	admin = models.ForeignKey(Admin)
	can_view = models.BooleanField(default=True)
	can_select_for_interview = models.BooleanField(default=True)
	can_select_for_position = models.BooleanField(default=True)
	can_fianlize_selection = models.BooleanField(default=True)	

# TODO: As we will have numbers from India only, pre set +91 and allow user to
# add other nos of phone no, rather than adding nos with +91.
class Subscribers(models.Model):
	phone_no = PhoneNumberField()
	def __str__(self):
		return str(self.phone_no)

class Application(models.Model):
	POSITION_CHOICES = (
		('w', "worker"),
		('h', "helper"),
	)
	GRADUATION_CHOICES = (
		('2', '7 pass'),
		('3', '10 pass'),
		('4', '12 pass'),
		('5', 'graduate'),
	)

	# In form, it should let user select first state, district and project and then
	# let them select center.
	center = models.ForeignKey(Center)
	for_position = models.CharField(max_length=1, choices=POSITION_CHOICES, default='w')
	applicant_name = models.CharField(max_length=250)
	# TODO: Same here for phone number field.
	phone_no = PhoneNumberField()
	graduation = models.CharField(max_length=1, choices=GRADUATION_CHOICES, default='D')
	is_married = models.BooleanField(default=True)
	home_distance_from_center = models.PositiveIntegerField(default=0)
	pincode_of_applicant = models.PositiveIntegerField(default=0)
	has_birth_certificate = models.BooleanField(default=False)
	has_marriage_certificate = models.BooleanField(default=False)
	has_ration_card = models.BooleanField(default=False)
	has_adhaar_card = models.BooleanField(default=False)
	digital_mark = models.PositiveIntegerField(default=0)
	# Is applicant selected for interview?
	is_selected_for_interview = models.BooleanField(default=False)
	# Is applicant selected after interview round?
	# If true, this applicants are the finally selected applicants.
	# TODO: Maybe we want to add some restrictions/validations after applicant is selected,
	# i.e. admins can not change their marking,
	is_selected_for_position = models.BooleanField(default=False)

	def __str__(self):
		return self.name

	# TODO: Change this digital marking system.
	# Wring digital marking function sepretly and call it here on save.
	# Change this system to give the points out of 10 for every information
	# First do check their eligiblity, if they are not eligible then do show
	# points but in red color or in negative, so non eligible applicant differs
	# from others applications.
	# TODO: Wring eligible function, which returns whether applicant is eligible
	# for given position or not.
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
