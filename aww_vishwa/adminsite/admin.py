from django.contrib import admin
from aww.models import (
	Center,
	Admin,
	Subscribers,
	Application,
)
# Register your models here.

class ApplicationAdmin(admin.ModelAdmin):
	list_display = ["center", "for_position", "applicant_name", "digital_mark",
	                "is_selected_for_interview", "is_selected_for_position"]
	class Meta:
		model = Application

admin.site.register(Admin)
admin.site.register(Subscribers)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Center)

