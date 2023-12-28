from django.urls import path
from . import views

app_name = "shelf"
urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search_partial, name="search_partial"),
]
