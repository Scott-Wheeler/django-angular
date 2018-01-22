from django.db import models
from django.utils import timezone

import datetime
from django.urls.base import reverse

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:author', kwargs={'pk': self.pk})


class Blog(models.Model):
    name = models.CharField(max_length=200)
    tagline = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('blog:blog', kwargs={'pk': self.pk})

    def get_blog_entries(self):
        return self.blogentry_set.all()
#         return BlogEntry.objects.filter(blog_id=self.pk)

    def get_published_entries(self):
        return self.blogentry_set.filter(
            pub_date__lte = timezone.now()
        )

class BlogEntry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField("date published")

#     author = models.ForeignKey(User)
    
    class Meta:
        verbose_name = "Blog entry"
        verbose_name_plural = "Blog entries"
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blogentry', kwargs={'pk': self.pk})


