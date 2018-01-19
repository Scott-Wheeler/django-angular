from django.urls import path

from . import views

## /blog/ has been stripped off by the root URLconf

## generic.DetailView expects the primary key to be pk

# app_name defines the application namespace
app_name = "blog"

urlpatterns = [
    # /blog/
    path("", views.IndexView.as_view(), name="index"),

    # /blog/5/
    path("<int:pk>/", views.BlogDetailView.as_view(), name="blog"),
    path("entry/<int:pk>/", views.BlogDetailView.as_view(), name="blogentry"),
    path("author/<int:pk>/", views.BlogDetailView.as_view(), name="author"),


#     # /blog/5/write/
#     path("<int:pk>/write/", views.DetailView.as_view(), name="detail"),

#     # /blog/5/save/
#     path("<int:pk>/save/", views.save_blog, name="save_blog"),

    # /blog/creation/
    path("creation/", views.BlogCreate.as_view(), name="blog_creation"),
    # /blog/updates/
    path("updates/", views.BlogUpdate.as_view(), name="blog_udpates"),
    # /blog/deletion/
    path("deletion/", views.BlogDelete.as_view(), name="blog_deletion"),

## maybe do the entry id through post instead
    # /blog/entry/creation/
    path("entry/creation/", views.BlogEntryCreate.as_view(), name="blogentry_creation"),
    # /blog/entry/updates/
    path("entry/updates/", views.BlogEntryUpdate.as_view(), name="blogentry_udpates"),
    # /blog/entry/deletion/
    path("entry/deletion/", views.BlogEntryDelete.as_view(), name="blogentry_deletion"),
    
## instead of passing it through the url with get
#     # /blog/42/creation/
#     path("<int:pk>/creation/", views.BlogEntryCreate.as_view(), name="blogentry_creation"),
#     # /blog/42/updates/
#     path("<int:pk>/updates/", views.BlogEntryUpdate.as_view(), name="blogentry_udpates"),
#     # /blog/42/deletion/
#     path("<int:pk>/deletion/", views.BlogEntryDelete.as_view(), name="blogentry_deletion"),


]




#     path("create/", views.mkblog, name="mkblog"),