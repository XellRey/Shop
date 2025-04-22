from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Addresses
# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("email", "first_name", "last_name", "is_staff")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Данные Ползователя", {"fields": ("first_name", "last_name")}),
        ("Разрешения", {"fields": ("is_active", "is_staff", "is_superuser")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "first_name", "last_name", "password1", "password2", "is_staff", "is_superuser"),
        }),
    )
admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Addresses)
class AddressesAdmin(admin.ModelAdmin):
    list_display = ('street', 'room', 'floor', 'code', 'entrance', 'comment')
