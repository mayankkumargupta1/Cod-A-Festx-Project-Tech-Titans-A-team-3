
from django.contrib import admin
from .admin import admin_site
from django.urls import path, include
from django.conf.urls.static import static
from . import settings


urlpatterns = [
    path('admin/', admin_site.urls),
    path('', include('users.urls')),
    path('', include('Home.urls')),
    path('', include('pages.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

