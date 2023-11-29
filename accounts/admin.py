from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, NationalIdentificationNumber, BasicInformation, BankVerificationNumber, NextOfKin

class CustomUserAdmin(UserAdmin):
    model = User
    add_form = UserCreationForm
    form = UserChangeForm
    list_display = (
        "username", "email", "first_name", "last_name", "phone_number", "is_superuser"
    )
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password", "username", "first_name", "last_name", "phone_number",)}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "username", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)
admin.site.register(User, CustomUserAdmin)


class NationalityAdmin(admin.ModelAdmin):
    list_display = (
        "user", "nin_number", "first_name", "last_name"
    )
admin.site.register(NationalIdentificationNumber, NationalityAdmin)

class BasicInformationAdmin(admin.ModelAdmin):
    list_display = (
        "user", "state", "local_government", "address", "phone_number",
        "date_of_birth"
    )
admin.site.register(BasicInformation, BasicInformationAdmin)

class BankVerificationAdmin(admin.ModelAdmin):
    list_display = (
        "user", "bvn_number", "first_name", "last_name", "date_of_birth"
    )
admin.site.register(BankVerificationNumber, BankVerificationAdmin)

class NextOfKinAdmin(admin.ModelAdmin):
    list_display = (
        "user", "first_name", "last_name", "relationship", "phone_number",
        "address", "nin_number"
    )
admin.site.register(NextOfKin, NextOfKinAdmin)