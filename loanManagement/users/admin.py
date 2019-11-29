from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

User = get_user_model()


# class UserAdmin(admin.ModelAdmin):
#     search_fields = ['email', 'username', 'phone_number']
#     form = UserAdminChangeForm
#     add_form = UserAdminCreationForm

admin.site.register(User)
