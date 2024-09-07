from django.shortcuts import render
from . import models
from Home.models import Navigation_link
# Create your views here.
def show_page(request, title):
    
    page = models.page.objects.filter(title=title).first()
    nav_link = Navigation_link.objects.all()
    context={
        'article': page,
        'Navigation_link' : nav_link
    }
    return render(request, 'page.html', context=context)