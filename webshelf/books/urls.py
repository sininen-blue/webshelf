from django.urls import path
from . import views

app_name = "books"
urlpatterns = [
    path("<int:book_id>/", views.index, name="index"),

    path("<int:book_id>/ch/<int:chapter_number>/", views.read_chapter, name="read_chapter"),

    path("<int:book_id>/add_review/", views.add_review, name="add_review"),
]
