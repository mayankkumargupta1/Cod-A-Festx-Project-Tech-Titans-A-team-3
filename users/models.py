from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from website.utils import compress_image
from django.core.exceptions import ValidationError

def validate_image_size(image):
    max_size_kb = 200  # Max size in KB
    if image.size > max_size_kb * 1024:  # Convert KB to Bytes
        raise ValidationError(f'Image file size must be under {max_size_kb} KB.')

class User(AbstractUser):
    user_id = models.UUIDField(default=uuid.uuid4, editable=False)
    STATUS = (
        ('Patient', 'Patient'),
        ('Subscriber', 'Subscriber'),
        ('Moderator', 'Moderator')
    )
    email = models.EmailField(unique=True)
    status = models.CharField(max_length=200, choices=STATUS, default='Patient')
    blood_group = models.CharField(max_length=3, default='', blank=True, null=True)
    age = models.IntegerField(null=True, blank=True)
    Gender = (('Male','Male'), ('Female','Female'), ('Other', 'Other'))
    gender = models.CharField(default='other', blank=True, null=True, choices=Gender, max_length=30)
    # Profile Picture
    profile_picture = models.ImageField(default='profile/default.png', upload_to='profile/',validators=[validate_image_size])
    _original_profile_picture = None

    def save(self, *args, **kwargs):
        if self.pk is not None:
            if self.profile_picture:
                validate_image_size(self.profile_picture)
            self._original_profile_picture = User.objects.get(pk=self.pk).profile_picture
            if self.profile_picture and self.profile_picture != self._original_profile_picture:
                self.profile_picture.name = f"{self.username}_profile_picture.jpg"
                compressed_image = compress_image(self.profile_picture)
                self.profile_picture = compressed_image
    
        super(User, self).save(*args, **kwargs)
    
        

    def __str__(self) -> str:
        return f'Name: {self.first_name}, status: {self.status}, email: {self.email}'

class tokens(models.Model):
    token = models.CharField(max_length=300)
    