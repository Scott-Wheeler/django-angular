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
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("create/<int:pk>/", views.create_blog, name="create_blog"),
    path("save/<int:pk>/", views.save_blog, name="save_blog"),
]