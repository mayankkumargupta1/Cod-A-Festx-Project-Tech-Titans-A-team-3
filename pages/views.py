from django.shortcuts import render
from . import models
from Home.models import Navigation_link, SocialMedia_and_HelpLine
# Create your views here.
def show_page(request, title):
    
    page = models.page.objects.filter(title=title).first()
    nav_link = Navigation_link.objects.all()
    socialMedia_and_HelpLine = SocialMedia_and_HelpLine.objects.first()

    context={
        'article': page,
        'Navigation_link' : nav_link,
        'SocialMedia_and_HelpLine': socialMedia_and_HelpLine
    }
    return render(request, 'page.html', context=context)