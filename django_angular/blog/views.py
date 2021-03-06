from django.shortcuts import render, get_object_or_404, reverse
from django import views
from django.views import View, generic
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.http.response import HttpResponse, HttpResponseRedirect

from django.utils import timezone
from django.db.models import Count

# Create your views here.

from .models import Blog, BlogEntry, Author
from .forms import BlogForm, BlogEntryForm, ContactForm
from django.http.request import HttpRequest


## what views do I need?
# CreateBlogView
# UpdateBlogView
# DeleteBlogView
# CreateBlogEntryView
# UpdateBlogEntryView
# DeleteBlogEntryView
# BlogListView
# BlogDetailView
# BlogEntryListView  ## should BlogEntryList be a part (or all) of BlogDetail?
# BlogEntryDetailView
# IndexView

## and for the generic views tutorial page Author and Contact
# ContactView
# AuthorCreate
# AuthorUpdate
# AuthorDelete

## Todo:
# AuthorListView
# AuthorDetailView



class AuthorCreate(CreateView):
    model = Author
    fields = ['name']
    template_name_suffix = "_creation"

class AuthorUpdate(UpdateView):
    model = Author
    fields = ['name']
    template_name_suffix = "_updates"

class AuthorDelete(DeleteView):
    model = Author
    fields = ['name']
    template_name_suffix = "_deletion"


class BlogCreate(CreateView):
    model = Blog
    fields = ['name', 'tagline']
    template_name_suffix = "_creation"

class BlogUpdate(UpdateView):
    model = Blog
    fields = ['name', 'tagline']
    template_name_suffix = "_updates"

class BlogDelete(DeleteView):
    model = Blog
    fields = ['name', 'tagline']
    template_name_suffix = "_deletion"


class BlogEntryCreate(CreateView):
    model = BlogEntry
    fields = ['title', 'text', 'pub_date']
    template_name_suffix = "_creation"

class BlogEntryUpdate(UpdateView):
    model = BlogEntry
    fields = ['title', 'text', 'pub_date']
    template_name_suffix = "_updates"

class BlogEntryDelete(DeleteView):
    model = BlogEntry
    fields = ['title', 'text', 'pub_date']
    template_name_suffix = "_deletion"


class ContactView(FormView):
    template_name = "about.html"
    form_class = ContactForm
    success_url = "/thanks/"
    
    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)
    













## index view as generic view (class based)
class IndexView(generic.ListView):
    template_name = "blog/index.html"
    context_object_name = "blogs"

    def get_queryset(self):
        """
        Get all Blogs that have published (in the past) BlogEntry(ies)
        Don't get blogs that have no entries or only have future entries
        order the blogs by the most recently published entry
        """
        return Blog.objects.filter(
            blogentry__pub_date__lte = timezone.now()  ## filter for blogs with entries in past
        ).annotate(
            Count("blogentry")
        ).filter(
            blogentry__gt = 0
        )


#         return Blog.objects.order_by("-id")
#         return Blog
    
    
    
#         ## TODO:
#         ## now this is working on Blog not BlogEntry, which has no pub_date,
#         ## it needs to order by the latest pub_date of its entries 
#         return Blog.objects.order_by("-pub_date")[:5]


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = "blog/author.html"


## detail view as generic view (class based)
class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = "blog/blog.html"
    
    ## pk is passed in as a kwarg
    def get(self, request, *args, **kwargs):
        blog = get_object_or_404(Blog, pk=kwargs['pk'])
#         entries = BlogEntry.objects.filter(blog_id=blog.pk)
        entries = blog.get_blog_entries()
        return render(request, "blog/blog.html", {'blog': blog, 'entries':entries})

#     ## pk == 8 is passed in as a kwarg
#     def get(self, request, *args, **kwargs):
# #         print("should say 8: ", kwargs['pk'])
#         blog = get_object_or_404(Blog, pk=kwargs['pk'])
# #         print("blog: " + repr(blog))
#         entries = BlogEntry.objects.filter(blog_id=blog.pk)
# #         entries = blog.get_blog_entries()
# #         print("blog entries: " + repr(entries))
# #         entries = Blog.blogentry_set.order_by("-pub_date")
#         return render(request, "blog/blog.html", {'blog': blog, 'entries':entries})
# #         return render(request, "blog:blog", {'blog': blog, 'entries':entries})

#         print("<~> ", request)
#         print("<~> ", kwargs)

class BlogEntryDetailView(generic.DetailView):
    model = BlogEntry
    template_name = "blog/blogentry.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


# save actions
def save_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)

    blog.name = request.POST["name"]
    blog.tagline = request.POST["tagline"]

    blog.save()

    return HttpResponseRedirect(reverse("blog:detail", args=(blog.id,)))


def save_entry(request, blog_entry_id):
    blog_entry = get_object_or_404(BlogEntry, pk=blog_entry_id)

    blog_entry.title = request.POST["title"]
    blog_entry.text = request.POST["text"]

    if not blog_entry.pub_date:
        # creating new 
        blog_entry.pub_date = timezone.now()

    blog_entry.save()

    return HttpResponseRedirect(reverse("blog:detail", args=(blog_entry.id,)))




# class BlogFormView(FormView):
#     ...
# 
# class BlogEntryFormView(FormView):
#     form_class = MyForm
#     initial = {'key': 'value'}
#     template_name = 'form_template.html'
# 
#     def get(self, request, *args, **kwargs):
#         form = self.form_class(initial=self.initial)
#         return render(request, self.template_name, {'form': form})
# 
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             # <process form cleaned data>
#             return HttpResponseRedirect('/success/')
# 
#         return render(request, self.template_name, {'form': form})




# class MakeBlog():
def mkblog(request):
    blog = Blog(name="", tagline="")
    return HttpResponseRedirect(reverse("blog:mkblog", args=(blog,)))
#     return render(request, "blog:create_blog", {"blog": blog})


def create_blog_entry(request):
    blog_entry = BlogEntry(title="", text="")
    return render(request, "blog:detail", {"blog_entry": blog_entry})


    





