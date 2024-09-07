from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),    
    path('ask', views.ai_text_generation_view, name='ask'),
    path('doctors', views.doctors, name='doctor'),
    path('ask-doctor/', views.ask_doctor_view, name='ask_doctor'),
    path('answer-received/', views.TemplateView.as_view(template_name='answer_received.html'), name='answer_received'),
    path('your-questions/', views.user_questions_view, name='user_questions'),
]