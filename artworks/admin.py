from django.contrib import admin
from artworks.models import *

admin.site.register(Artwork)
admin.site.register(Category)
admin.site.register(Artist)
admin.site.register(Project)