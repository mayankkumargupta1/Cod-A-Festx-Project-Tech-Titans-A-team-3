from website.admin import admin_site
# Register your models here.
from .models import *

admin_site.register(announcement)
admin_site.register(Navigation_link)
admin_site.register(Navigation_link2)
admin_site.register(Team_member)

admin_site.register(SocialMedia_and_HelpLine)
admin_site.register(footer_and_home_page_data)