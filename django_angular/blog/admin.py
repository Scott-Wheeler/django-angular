from django.contrib import admin

# Register your models here.
from .models import Blog, BlogEntry

admin.site.register(Blog)
admin.site.register(BlogEntry)