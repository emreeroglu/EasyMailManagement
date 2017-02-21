from django.contrib import admin
from common.models import User
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    """Custom user in Django Admin."""
    list_display = ('pk', '__str__', 'email', 'username', 'created_date',)
    list_filter = ('groups',)
    fieldsets = (
        ('Account Info', {
            'fields': ('first_name', 'last_name', 'username', 'email',
                       'groups', 'is_staff', 'is_active',)
        }),
        ('Extra Details', {
            'fields': ('mobile',)
        }),
        ('Password', {
            'fields': ('password',)
        }),
    )

admin.site.register(User, CustomUserAdmin)
