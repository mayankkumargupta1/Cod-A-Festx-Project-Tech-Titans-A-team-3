from website.admin import admin_site
from .models import *

admin_site.register(payment)
admin_site.register(subscription)