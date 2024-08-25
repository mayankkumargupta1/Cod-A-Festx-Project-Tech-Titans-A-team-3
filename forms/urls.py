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
    path('arogya_view', view=views.arogya_view, name='arogya_view'),
    path('clean_india_view', view=views.clean_india_view, name='clean_india_view'),
    path('rakt_veer_view', view=views.rakt_veer_view, name='rakt_veer_view'),
    path('judicial_help_view', view=views.judicial_help_view, name='judicial_help_view'),
    path('kanya_daan_view', view=views.kanya_daan_view, name='kanya_daan_view'),
    path('shiksha_sankalp_view', view=views.shiksha_sankalp_view, name='shiksha_sankalp_view'),
    path('employment_generation_view', view=views.employment_generation_view, name='employment_generation_view'),
    path('road_safety_view', view=views.road_safety_view, name='road_safety_view'),
    path('cancer_awareness_view', view=views.cancer_awareness_view, name='cancer_awareness_view')
]



urlpatterns += [path('download', view=forms_download_views.export_full_database_as_excel, name='download_model'),
                path('',forms_download_views.forms, name='forms')]