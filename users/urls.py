from django.urls import path
from .views import *

urlpatterns = [
    path('register/', Register, name = 'register'),
    path('login/', c_login, name='login'),
    path('logout/', c_logout, name='logout'),
    path('profile/<username>', profile, name='profile'),
    path('update', update_profile, name='update_profile'),
    path('activate/<uidb64>/<token>', activate, name='activate'),
    path("password_reset", password_reset_request, name="password_reset"),
    path('reset/<uidb64>/<token>', passwordResetConfirm, name='password_reset_confirm'),
]
