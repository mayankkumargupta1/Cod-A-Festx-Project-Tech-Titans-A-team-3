from django.urls import path
from . import views
from . import forms_download_views

urlpatterns = [
    path('your_problem', view = views.Your_problem, name='your_problem'),
    path('your_suggestion', view = views.Your_suggestion, name='your_suggestion'),
    path('doctors_panel', view=views.doctors_panel, name='doctors_panel'),
    path('hospital_panel', view=views.hospital_panel, name='hospital_panel'),
    path('volunteer', view=views.Volunteer_panel, name='volunteer_panel'),
    path('arogya_yojana', view=views.arogya_yojana, name='arogya_yojana'),
    path('judicial_help_panel', view=views.judicial_help_panel, name='judicial_help_panel'),
    path('plantation', view=views.plantation, name='plantation'),
    path('save_water', view=views.save_water, name='save_water'),

]



urlpatterns += [path('download', view=forms_download_views.export_full_database_as_excel, name='download_model'),]