from django.urls import path
from . import views

app_name = "desk"
urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("create_chapter", views.create_book, name="create_book"),
    path("view_book/<int:book_id>", views.view_book, name="view_book"),
    path("update_book/<int:book_id>", views.update_book, name="update_book"),
    path("delete_book/<int:book_id>", views.delete_book, name="delete_book"),

    path("create_chapter/<int:book_id>", views.create_chapter, name="create_chapter"),
]
