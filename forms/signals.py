from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import *
from .utils import *

@receiver(pre_delete, sender=Your_problem_form)
def before_delete_my_model(sender, instance, **kwargs):
    try:
        document_id = get_file_id(instance.document)
        delete_file(document_id)
    except:
        pass
    try:
        image_id = get_file_id(instance.picture)
        delete_file(image_id)
    except:
        pass

@receiver(pre_delete, sender=Your_suggestion_form)
def before_delete_my_model(sender, instance, **kwargs):
    try:
        document_id = get_file_id(instance.document)
        delete_file(document_id)
    except:
        pass
    try:
        image_id = get_file_id(instance.picture)
        delete_file(image_id)
    except:
        pass


@receiver(pre_delete, sender=doctors_panel_form)
def before_delete_my_model(sender, instance, **kwargs):
    try:
        document_id = get_file_id(instance.document)
        delete_file(document_id)
    except:
        pass
    try:
        image_id = get_file_id(instance.picture)
        delete_file(image_id)
    except:
        pass


@receiver(pre_delete, sender=hospital_panel_form)
def before_delete_my_model(sender, instance, **kwargs):
    try:
        document_id = get_file_id(instance.document)
        delete_file(document_id)
    except:
        pass
    try:
        image_id = get_file_id(instance.picture)
        delete_file(image_id)
    except:
        pass