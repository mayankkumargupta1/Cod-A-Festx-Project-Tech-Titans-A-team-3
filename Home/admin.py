from website.admin import admin_site
# Register your models here.
from .models import *
admin_site.register(Navigation_link)
admin_site.register(Navigation_link2)
admin_site.register(health_tip)
admin_site.register(doctor)
admin_site.register(specialization)
admin_site.register(ask_doctor)