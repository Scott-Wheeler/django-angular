from django.contrib import admin

# Register your models here.
from .models import Blog, BlogEntry, Author

class BlogEntryInline(admin.StackedInline):
    model = BlogEntry
    extra = 1


class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["name", "tagline"]})
    ]

    inlines = [BlogEntryInline]

    list_display = ["name", "tagline"]
#     list_filter = ["blogentry_set__pub_date"]
    search_fields = ["name", "tagline"]
    

admin.site.register(Blog, BlogAdmin)
# admin.site.register(Blog)
# admin.site.register(BlogEntry)


admin.site.register(Author)