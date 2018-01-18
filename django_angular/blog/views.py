from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic

# Create your views here.

from .models import BlogEntry
from django.utils import timezone

## index view as generic view (class based)
class IndexView(generic.ListView):
    template_name = "blog/index.html"
    context_object_name = "latest_blog_entries"
    
    def get_queryset(self):
        return BlogEntry.objects.order_by("-pub_date")[:5]


## detail view as generic view (class based)
class DetailView(generic.DetailView):
    model = BlogEntry
    template_name = "blog/detail.html"


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


def create_blog(request):
    blog = Blog(name="", tagline="")
    return render(request, "blog:create_blog", {"blog": blog})


def create_blog_entry(request):
    blog_entry = BlogEntry(title="", text="")
    return render(request, "blog:detail", {"blog_entry": blog_entry})


    





