from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import gallery_image, gallery_new
from forms.utils import *

@receiver(pre_delete, sender=gallery_image)
def before_delete_my_model(sender, instance, **kwargs):
    try:
        image_id = get_file_gallery_id(instance.url)
        delete_file(image_id)
    except:
        pass

@receiver(pre_delete, sender=gallery_new)
def before_delete_my_news(sender, instance, **kwargs):
    try:
        image_id = get_file_gallery_id(instance.url)
        delete_file(image_id)
    except:
        pass