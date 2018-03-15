from django.contrib import admin
from aww.models import (
	Center,
	Admin,
	Subscribers,
	Vacancy,
	Application,
)
# Register your models here.

class ApplicationAdmin(admin.ModelAdmin):
	list_display = ["center", "for_position", "name", "digital_mark", "is_selected"]
	class Meta:
		model = Application

admin.site.register(Admin)
admin.site.register(Subscribers)
admin.site.register(Vacancy)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Center)

