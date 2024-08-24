from django.contrib import admin
from website.admin import admin_site
# Register your models here.
from .models import *
admin_site.register(gallery_image)
admin_site.register(gallery_new)