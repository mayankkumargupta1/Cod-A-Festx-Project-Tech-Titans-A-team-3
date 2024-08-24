from django.urls import path
from .views import generate, verify

urlpatterns = [
    path('generate/<uuid:id>/', generate, name='generate'),
    path('verify/<uuid:id>/', verify, name='verify')
]
