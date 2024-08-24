from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

class page(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = RichTextField()  # This will use CKEditor for the content field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Name: '+self.title+' url: ' +  reverse('pages', kwargs={'title': str(self.title)})