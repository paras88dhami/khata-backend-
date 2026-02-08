from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "phone", "full_name", "is_active", "is_staff")
    search_fields = ("email", "phone", "full_name")
    ordering = ("-created_at",)
