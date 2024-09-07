from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import *
from website.settings import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from users.models import User
from .forms import *
import os
import google.generativeai as genai
import markdown2
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
# Create your views here.
def Home(request):
    nav_link = Navigation_link.objects.all()
    nav_link2 = Navigation_link2.objects.all()
    tips = health_tip.objects.all()
    context = {

        'Navigation_link' : nav_link,
        'Navigation_link2' : nav_link2,
        'tip' : tips,

    }
    return render(request=request, template_name='index.html', context=context)


genai.configure(api_key=GOOGLE_API_KEY)
def generate_text(prompt):
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        html_text = markdown2.markdown(response.text)
        return html_text
    except Exception as e:
        return str(e)
    
@login_required(login_url='/login/')
def ai_text_generation_view(request):
    generated_text = None
    if request.method == 'POST':
        form = TextGenerationForm(request.POST)
        if form.is_valid():
            prompt =  'Behave as a professinal Doctor who is serious, do not entertain anything except topics related to health. Incase of major problems suggest Doctor consultation. Give long answers. PROBLEM: ' + form.cleaned_data['prompt'] 
            generated_text = generate_text(prompt)  # Call the Google Generative AI function
    else:
        form = TextGenerationForm()

    nav_link = Navigation_link.objects.all()
    nav_link2 = Navigation_link2.objects.all()
    return render(request, 'text_generation.html', {
        'form': form,
        'generated_text': generated_text,
        'Navigation_link' : nav_link,
        'Navigation_link2' : nav_link2,
    })


@login_required(login_url='/login/')
def doctors(request):
    doctors = doctor.objects.prefetch_related('specialization').all()
    nav_link = Navigation_link.objects.all()
    nav_link2 = Navigation_link2.objects.all()
    context = {
        'doctors' : doctors,
        'Navigation_link' : nav_link,
        'Navigation_link2' : nav_link2
    }
    return render(request, 'doctors.html', context=context)

@login_required(login_url='/login/')
def ask_doctor_view(request):
    nav_link = Navigation_link.objects.all()
    nav_link2 = Navigation_link2.objects.all()
    if request.method == 'POST':
        form = AskDoctorForm(request.POST)
        if form.is_valid():
            ask_doctor_instance = form.save(commit=False)
            ask_doctor_instance.user = request.user
            ask_doctor_instance.save()
            return redirect('answer_received')
    else:
        form = AskDoctorForm()
    
    return render(request, 'ask_doctor.html', {'form': form,'Navigation_link' : nav_link, 'Navigation_link2' : nav_link2,})

def user_questions_view(request):
    nav_link = Navigation_link.objects.all()
    nav_link2 = Navigation_link2.objects.all()
    questions = ask_doctor.objects.filter(user=request.user)
    return render(request, 'user_questions.html', {'questions': questions, 'Navigation_link' : nav_link,'Navigation_link2' : nav_link2,})