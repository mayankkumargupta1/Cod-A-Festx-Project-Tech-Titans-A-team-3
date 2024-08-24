from django.contrib import admin
from .models import User
from website.admin import admin_site
from website.admin import CustomUserAdmin
# Register your models here.

admin_site.register(User, CustomUserAdmin)