from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from time import gmtime, strftime

def image_name(instance, filename):
    return "artworks/images/%s_%s" % (strftime('%d-%m-%Y', gmtime()), filename)

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return "/artworks/category/%s/" % self.slug

class Artwork(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    text = models.TextField(max_length=1000, null=True, blank=True)
    category = models.ManyToManyField(Category)
    author = models.ManyToManyField(User)
    time = models.DateTimeField(default=datetime.now)
    latitude = models.CharField(max_length=500, null=True, blank=True)
    longitude = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to=image_name)
    image_2 = models.ImageField(upload_to=image_name, null=True, blank=True)
    image_3 = models.ImageField(upload_to=image_name, null=True, blank=True)
    image_4 = models.ImageField(upload_to=image_name, null=True, blank=True)
   
    def __unicode__(self):
        return "%i %s" % (self.id, self.title)

    def get_absolute_url(self):
        return "/artworks/%i/" % self.id

def avatar_name(instance, filename):
    return "artists/images/%s_%s" % (strftime('%d-%m-%Y', gmtime()), filename)

class Artist(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    nickname = models.CharField(max_length=255, null=True, blank=True)
    site = models.CharField(max_length=255, null=True, blank=True)
    site_name = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(max_length=1000, null=True, blank=True)
    avatar = models.ImageField(upload_to=avatar_name, null=True, blank=True)
    
    def name(self):
        if not self.nickname:
            return self.first_name
        else:
            return self.nickname
    
    def __unicode__(self):
        if (self.first_name and self.last_name):
            return "%s %s" % (self.first_name, self.last_name)
        else:
            return self.user.username

class Project(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to=image_name, null=True, blank=True)
    artwork = models.ManyToManyField(Artwork)
    author = models.ManyToManyField(User)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/artworks/%s/" % self.slug

