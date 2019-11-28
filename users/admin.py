from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    # 내장된 UserAdmin.fieldsets과 Custom한 fieldsets를 합쳐주어야 함
    fieldsets = UserAdmin.fieldsets + (
        ("ZZIGSA", {"fields": ("nickname", "zzigsa",)},),
    )
