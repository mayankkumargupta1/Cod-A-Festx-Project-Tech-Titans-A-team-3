from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_order, name='create_order'),
    path('payment_callback', views.payment_callback, name='payment_callback'),
]
