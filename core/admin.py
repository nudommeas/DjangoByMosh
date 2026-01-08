from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin # import this when using Custom Models
from .models import User
# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # If you are using a fully custom user model, you will need to define its admin class and register it appropriately.
    # You can modify the admin configuration, if you're extending the default User Model. 
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "usable_password", "password1", "password2", "email", "first_name", "last_name"),
            },
        ),
    )