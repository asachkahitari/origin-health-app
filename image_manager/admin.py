from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Image, CustomUser

# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'role', 'is_staff']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Image)