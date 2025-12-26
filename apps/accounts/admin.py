from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):

    list_display = (
        'first_name',
        'last_name',
        'email',
        'is_staff',
        'is_active',
        'created_at',
    )

    ordering = ('email',)

    fieldsets = (
        ('Personal Info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Important Dates', {
            'fields': ('last_login', )
        }),
    )
