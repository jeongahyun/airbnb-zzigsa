from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "zzigsa",
                )
            },
        ),
    )

    list_filter = UserAdmin.list_filter + ("zzigsa",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "zzigsa",
        "is_staff",
        "is_superuser",
    )
