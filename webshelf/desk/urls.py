from django.urls import path
from . import views

app_name = "desk"
urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("add-book", views.create_book, name="create_book"),
    path("view-book/<int:book_id>", views.view_book, name="view_book"),
    path("update-book/<int:book_id>", views.update_book, name="update_book"),
    path("delete-book/<int:book_id>", views.delete_book, name="delete_book"),
]
