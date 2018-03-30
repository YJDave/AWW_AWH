from django.contrib.auth.models import User
from .models import (
	Center,
	Admin,
	Admin_CDPO,
	Admin_TDO,
	Admin_DeputyCollector,
	Subscribers,
	Application,
	Project,
	State,
	District,
)

def fill_intial_data():
	USER_COMMON_PASSWORD = "aww123123"
	COMMON_PINCODE = 364002
	USERS = ["YASHASHVI", "PINAL", "STUTI", "ANERI", "ARCHITA", "BANSI"]
	STATES = ["Gujarat", "Maharashtra", "Delhi"]

	# First create super users to login
	for user in USERS:
		user = User.objects.create(username=user, password=USER_COMMON_PASSWORD)

	# Ceate state, districts, projects
	for state in STATES:
		state_obj = State.objects.create(name=state)
		common_district_name = state[0:3] + " dis "
		for i in range(0, 2):
			dis_name = common_district_name + str(i)
			dis_obj = District.objects.create(state=state_obj, name=dis_name)
			common_proj_name = dis_name + " proj "
			for j in range(0, 2):
				proj_name = common_proj_name + str(j)
				proj_obj = Project.objects.create(state=state_obj, district=dis_obj, name=proj_name)

				# Create admins
				if (state == STATES[0]):
					admin1 = Admin.objects.create(project=proj_obj, user=User.objects.filter(username=USERS[0])[0])
					admin2 = Admin.objects.create(project=proj_obj, user=User.objects.filter(username=USERS[1])[0])
					admin3 = Admin.objects.create(project=proj_obj, user=User.objects.filter(username=USERS[2])[0])
				elif (state == STATES[1]):
					admin1 = Admin.objects.create(project=proj_obj, user=User.objects.filter(username=USERS[3])[0])
					admin2 = Admin.objects.create(project=proj_obj, user=User.objects.filter(username=USERS[4])[0])
					admin3 = Admin.objects.create(project=proj_obj, user=User.objects.filter(username=USERS[5])[0])
				elif (state == STATES[2]):
					admin1 = Admin.objects.create(project=proj_obj, user=User.objects.filter(username=USERS[0])[0])
					admin2 = Admin.objects.create(project=proj_obj, user=User.objects.filter(username=USERS[2])[0])
					admin3 = Admin.objects.create(project=proj_obj, user=User.objects.filter(username=USERS[5])[0])
				Admin_TDO.objects.create(admin=admin1)
				Admin_CDPO.objects.create(admin=admin2)
				Admin_DeputyCollector.objects.create(admin=admin3)
				# Create Centers
				for k in range(0, 2):
					center_obj = Center.objects.create(state=state_obj, district=dis_obj, project=proj_obj,
									  	  sector=k, pincode=COMMON_PINCODE, name=str(k) + " center",
									  	  center_no=i*k*j)

					# Create applications
					Application.objects.create(center=center_obj, for_position="worker", applicant_name="ABACD",
						                       phone_no="+919292987867", graduation="12 pass", is_married=True,
						                       home_distance_from_center=5, pincode_of_applicant=COMMON_PINCODE,
						                       has_birth_certificate=True, has_marriage_certificate=False,
						                       has_ration_card=False, has_adhaar_card=True)

					Application.objects.create(center=center_obj, for_position="helper", applicant_name="welkm",
						                       phone_no="+919292987867", graduation="12 pass", is_married=True,
						                       home_distance_from_center=10, pincode_of_applicant=COMMON_PINCODE,
						                       has_birth_certificate=False, has_marriage_certificate=True,
						                       has_ration_card=True, has_adhaar_card=True)

if __name__ == "__main__":
	fill_intial_data()
