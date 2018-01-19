from django.contrib import admin

# Register your models here.
from .models import Blog, BlogEntry, Author

admin.site.register(Blog)
admin.site.register(BlogEntry)
admin.site.register(Author)