from django.db import models

# Create your models here.
class gallery_image(models.Model):
    url = models.URLField()
    category = models.CharField(max_length=400)
    def __str__(self) -> str:
        return f'category: {self.category}, url: {self.url}'
class gallery_new(models.Model):
    url = models.URLField()
    category = models.CharField(max_length=400)
    def __str__(self) -> str:
        return f'category: {self.category}, url: {self.url}'