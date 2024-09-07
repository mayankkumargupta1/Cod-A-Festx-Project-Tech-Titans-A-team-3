from django.db import models
from django.shortcuts import redirect
from website.utils import compress_image
from django.contrib import messages
from users.models import User

class health_tips(models.Model):
    announcement = models.TextField(null=False)
    link = models.URLField(null=True, blank=True)

    def __str__(self) -> str:
        return str(self.announcement)
    
class Navigation_link(models.Model):
    Name = models.CharField(max_length=200, null=False)
    Url = models.URLField(null=False)

    def __str__(self) -> str:
        return str(self.Name)
    
class Navigation_link2(models.Model):
    Name = models.CharField(max_length=200, null=False)
    Url = models.URLField(null=False)

    def __str__(self) -> str:
        return str(self.Name)

class health_tip(models.Model):
    tip = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.tip
    
    def save(self, *args, **kwargs):
        if not self.pk and health_tip.objects.exists():
            return redirect('/admin/Home/')
        return super(health_tip, self).save(*args, **kwargs)
    

class specialization(models.Model):
    specialization = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.specialization


class doctor(models.Model):
    profile_picture = models.URLField(default='https://drive.google.com/thumbnail?id=1tnvzDrM46Rdih8Kvg_wFYYpm1ht-0yyp&sz=s4000')
    full_name = models.CharField(max_length=200)
    specialization = models.ManyToManyField(specialization, related_name='doctors')
    phone_no = models.CharField(max_length=200)
    email = models.EmailField(default=None, null=True)
    experience = models.IntegerField()
    work = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.full_name
    
class ask_doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    question = models.TextField(max_length=2000)
    answer = models.TextField(max_length=5000)
    answered_at = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return self.question
