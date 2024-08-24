from django.shortcuts import render, HttpResponse
from .models import gallery_image, gallery_new
from forms.utils import gallery_image_url, get_file_gallery_id
from users.decorators import user_not_superuser
from Home.models import Navigation_link

# Create your views here.
def gallery(request, category = 'all'):
    if category == 'all':
        gallery_obj = gallery_image.objects.all()
    else:
        gallery_obj = gallery_image.objects.filter(category=category)

    nav_link = Navigation_link.objects.all()
    categories = gallery_image.objects.values_list('category', flat=True).distinct()
    context = {
        'images' : gallery_obj,
        'categories' : categories,
        'Navigation_link' : nav_link,
    }
    return render(request,'gallery.html', context=context)

def news(request, category = 'all'):
    if category == 'all':
        gallery_obj = gallery_new.objects.all()
    else:
        gallery_obj = gallery_new.objects.filter(category=category)
    
    nav_link = Navigation_link.objects.all()
    categories = gallery_new.objects.values_list('category', flat=True).distinct()
    context = {
        'images' : gallery_obj,
        'categories' : categories,
        'Navigation_link' : nav_link,
    }
    return render(request,'gallery_news.html', context=context)


@user_not_superuser
def gallery_upload(request):
    if request.method == 'POST':
        files = request.FILES.getlist('images')
        category = request.POST.get('category')
        for file in files:
            obj = gallery_image(
                url= gallery_image_url(file),
                category = category
            )
            obj.save()
            
        return render(request, 'gallery_success.html')
    return render(request, 'upload_images.html')

@user_not_superuser
def news_upload(request):
    if request.method == 'POST':
        files = request.FILES.getlist('images')
        category = request.POST.get('category')
        for file in files:
            obj = gallery_new(
                url= gallery_image_url(file),
                category = category
            )
            obj.save()
            
        return render(request, 'gallery_success.html')
    return render(request, 'upload_images.html')