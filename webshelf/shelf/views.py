from django.shortcuts import render
from books.models import Book


def index(request):
    latest = Book.objects.order_by("created_date")[:20]
    context = {
        "latest_book_list": latest,
    }
    return render(request, "shelf/index.html", context)


def search_partial(request):
    return render(request, "search-partial.html")
