from django.shortcuts import render, HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .utils import Generate_id_card
from users.models import User
from gallery.models import gallery_image
from payments import models as pay

# Create your views here.
def Home(request):
    anounce = announcement.objects.all()
    nav_link = Navigation_link.objects.all()
    nav_link2 = Navigation_link2.objects.all()
    team_members = Team_member.objects.all()[:5]
    socialMedia_and_HelpLine = SocialMedia_and_HelpLine.objects.first()
    last_gallery_images = gallery_image.objects.order_by('-id')[:6]
    gallery_3 = last_gallery_images[:3]
    gallery_6 = last_gallery_images[3:6]
    
    data = footer_and_home_page_data.objects.first()
    context = {
        'announcement' : anounce,
        'Navigation_link' : nav_link,
        'Navigation_link2' : nav_link2,
        'Team_members' : team_members,
        'SocialMedia_and_HelpLine': socialMedia_and_HelpLine,
        'gallery_3' : gallery_3,
        'gallery_6' : gallery_6,
        'data' : data
    }
    return render(request=request, template_name='index.html', context=context)

def team_members(request):
    nav_link = Navigation_link.objects.all()
    context = {
        'Navigation_link' : nav_link,
        'team_members':Team_member.objects.all()}
    return render(request, 'team_members.html', context=context)

@login_required(login_url='/login/')
def id_card_page(request):
    if request.POST:
        if pay.payment.objects.filter(user= request.user).exists() == False:
            return redirect('create_order/')
        else:
            id = request.user.id
            user = User.objects.get(pk=id)
            relative_url = reverse('profile', kwargs={'username': str(user.username)})
            URL = str(request.build_absolute_uri(relative_url))
            FULL_NAME = str(user.first_name) + ' ' + str(user.last_name)
            STATUS = str(user.status)
            DATE = str(user.date_joined).split()[0]
            PIC = user.profile_picture
            buffer = Generate_id_card(URL, FULL_NAME, STATUS, DATE, PIC)

            response = HttpResponse(buffer, content_type='image/png')
            response['Content-Disposition'] = 'attachment; filename="{}.png"'.format(str(user.username))
            return response

    if request.user:
        if pay.payment.objects.filter(user= request.user).exists() == False:
            return redirect('create_order/')
        else:
            user = User.objects.get(pk=request.user.id)
            if str(user.profile_picture.url) == '/media/profile/default.png':
                messages.error(request, 'PLEASE UPDATE YOUR PROFILE PICTURE')
                return redirect(reverse('update_profile'))
            else:
                return render(request, 'id_card.html', context={
                    'Navigation_link' : Navigation_link.objects.all(),
                    'SocialMedia_and_HelpLine': SocialMedia_and_HelpLine.objects.all()
                })