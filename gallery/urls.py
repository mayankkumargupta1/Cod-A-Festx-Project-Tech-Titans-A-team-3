from django.urls import path
from .views import *

urlpatterns = [
    path('name/<category>', gallery, name='gallery'),
    path('upload', gallery_upload, name='gallery_upload'),
    path('news/<category>', news, name='news'),
    path('upload_news', news_upload, name='news_upload')
]
