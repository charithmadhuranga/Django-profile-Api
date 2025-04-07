from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from profile_api import models

# Register your models here.
class UserProfileAdmin(UserAdmin):
    """User Profile Admin"""
    list_display = ('email','first_name','last_name','is_superuser','is_staff')
    readonly_fields = ('created_at','updated_at','last_login')
    ordering = ('-created_at',)
    list_filter = ('is_superuser','is_staff')
    search_fields = ('email',)
    filter_horizontal = ()
    fieldsets = ()


admin.site.register(models.UserProfile, UserProfileAdmin)
