from django.urls import path
from . import views
urlpatterns = [
    path('pages/<title>', views.show_page, name='pages')
]
