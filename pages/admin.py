from django.contrib import admin
from website.admin import admin_site
from .models import page
from ckeditor.widgets import CKEditorWidget
from django import forms

class PageForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = page
        fields = '__all__'

class PageAdmin(admin.ModelAdmin):
    form = PageForm

admin_site.register(page, PageAdmin)