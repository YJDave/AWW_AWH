from django.contrib import admin
from aww.models import (
	Center,
	Admin,
	Subscribers,
	Vacancy,
	Application,
)
# Register your models here.

admin.site.register(Admin)
admin.site.register(Subscribers)
admin.site.register(Vacancy)
admin.site.register(Application)
admin.site.register(Center)
