
from django.contrib import admin
from .admin import admin_site
from django.urls import path, include
from django.conf.urls.static import static
from . import settings


urlpatterns = [
    path('admin/', admin_site.urls),
    path('', include('users.urls')),
    path('', include('Home.urls')),
    path('forms/', include('forms.urls')),
    path('', include('pages.urls')),
    path('gallery/', include(('gallery.urls', 'gallery'), namespace='gallery')),
    path('create_order/', include(('payments.urls', 'payments'), namespace='payments')),
    path('certificates/', include(('certificates.urls', 'certificates'), namespace='certificates')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

