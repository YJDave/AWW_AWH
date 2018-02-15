from django.contrib import admin
from .models import (
	AppUser,
)

# Register your models here.

class AppUserAdmin(admin.ModelAdmin):
	list_display = ["user", "joined_date", "legal_name"]
	class Meta:
		model = AppUser

admin.site.register(AppUser, AppUserAdmin)
