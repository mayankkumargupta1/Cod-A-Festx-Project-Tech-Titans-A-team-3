from django.db import models
from django.shortcuts import redirect
from website.utils import compress_image
from django.contrib import messages


class announcement(models.Model):
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

class Team_member(models.Model):
    Image = models.ImageField(upload_to='team/', null=False)
    Name = models.CharField(max_length=250)
    Position = models.CharField(max_length=200)
    Organization = models.CharField(max_length=400)
    linkedin = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    def save(self, *args, **kwargs):
        compressed_image = compress_image(self.Image)
        self.Image = compressed_image
        super(Team_member, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return 'NAME: '+ str(self.Name) +' POSITION: '+ str(self.Position)
    
class SocialMedia_and_HelpLine(models.Model):
    facebook = models.URLField(max_length=255, blank=True, null=True)
    twitter = models.URLField(max_length=255, blank=True, null=True)
    linkedin = models.URLField(max_length=255, blank=True, null=True)
    instagram = models.URLField(max_length=255, blank=True, null=True)
    youtube = models.URLField(max_length=255, blank=True, null=True)
    helpline_no = models.CharField(max_length=20, null=False)

    def save(self, *args, **kwargs):
        if not self.pk and SocialMedia_and_HelpLine.objects.exists():
            return redirect('/admin/Home/socialmedia_and_helpline/')
        return super(SocialMedia_and_HelpLine, self).save(*args, **kwargs)

    def __str__(self):
        return "Social Media Links"

    class Meta:
        verbose_name = "Social Media Links"
        verbose_name_plural = "Social Media Links and HelpLine Number"

class footer_and_home_page_data(models.Model):
    people_got_clothes = models.IntegerField()
    handicaps_got_help = models.IntegerField()
    people_got_medical_help = models.IntegerField()

    become_a_partner_link = models.URLField(blank=True,null=True)
    donate_to_support_link = models.URLField(blank=True,null=True)
    about_us_link = models.URLField(blank=True,null=True)
    
    def save(self, *args, **kwargs):
        if not self.pk and footer_and_home_page_data.objects.exists():
            return redirect('/admin/Home/')
        return super(footer_and_home_page_data, self).save(*args, **kwargs)