import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
from django.apps import apps
from users import decorators
import io

@decorators.user_not_superuser
def export_full_database_as_excel(request):
    
    buffer = io.BytesIO()

    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        models = apps.get_models()
        for model in models:
            
            data = model.objects.all().values()

            df = pd.DataFrame(list(data))

            if df.empty:
                continue
            for col in df.select_dtypes(include=['datetimetz']).columns:
                df[col] = df[col].dt.tz_convert(None)

            df.to_excel(writer, sheet_name=model._meta.model_name, index=False)

    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=full_database.xlsx'
    
    return response


from Home.models import Navigation_link
def forms(request):
    nav_link = Navigation_link.objects.all()
    form = [
    'your_problem',
    'your_suggestion',
    'doctors_panel',
    'hospital_panel',
    'volunteer_panel',
    'arogya_yojana',
    'judicial_help_panel',
    'plantation',
    'save_water',
    'arogya_view',
    'clean_india_view',
    'rakt_veer_view',
    'judicial_help_view',
    'kanya_daan_view'
    ]
    context = {
        'Navigation_link': nav_link,
        'forms' : form
    }
    return render(request, 'forms.html', context = context)