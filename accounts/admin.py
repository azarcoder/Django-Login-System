from django.contrib import admin
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.

class CustomAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ["username", "age", "contact", "is_staff", "city"]
    fieldsets = (
        (None, {"fields": ("username", "password", "email", "age", "contact", "city")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    # Fields for adding new users
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "age",
                    "contact",
                    "city"
                ),
            },
        ),
    )

admin.site.register(CustomUser, CustomAdmin)
