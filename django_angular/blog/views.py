from django.shortcuts import render, get_object_or_404, reverse
from django import views
from django.views import View, generic
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.http.response import HttpResponse, HttpResponseRedirect
from django.utils import timezone

# Create your views here.

from .models import Blog, BlogEntry, Author
from .forms import BlogForm, BlogEntryForm, ContactForm


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
    context_object_name = "latest_blog_entries"
    
    def get_queryset(self):
        return BlogEntry.objects.order_by("-pub_date")[:5]


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = "blog/author.html"


## detail view as generic view (class based)
class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = "blog/blog.html"


class BlogEntryDetailView(generic.DetailView):
    model = BlogEntry
    template_name = "blog/blogentry.html"




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


    





