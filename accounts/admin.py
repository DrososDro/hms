from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, Group
from .models import Account, Perm

# Register your models here.


class MyCustomAdmin(UserAdmin):
    list_display = ("email", "last_login", "date_joined")
    list_filter = ()
    fieldsets = (
        (None, {"fields": ("email", "username", "password")}),
        ("Personal Info", {"fields": ("name", "surname", "phone")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_admin",
                    "is_superadmin",
                    "is_mechanic",
                    "is_active",
                    "permissions",
                )
            },
        ),
        ("Details", {"fields": ("last_login", "date_joined")}),
    )
    filter_horizontal = ()
    search_fields = ("email",)
    readonly_fields = ("last_login", "date_joined")


admin.site.unregister(Group)
admin.site.register(Account, MyCustomAdmin)
admin.site.register(Perm)
