
# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserProfile


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("LearnHub Information", {"fields": ("role",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("LearnHub Information", {"fields": ("role",)}),
    )


admin.site.register(UserProfile)