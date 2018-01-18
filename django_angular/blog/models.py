from django.db import models
from django.utils import timezone

import datetime

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class BlogEntry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField("Blog Entry Title", max_length=200)
    text = models.TextField("blog entry text")
    pub_date = models.DateTimeField("date published")

#     author = models.ForeignKey(User)
    
    class Meta:
        verbose_name = "Blog entry"
        verbose_name_plural = "Blog entries"
    
    def __str__(self):
        return self.title