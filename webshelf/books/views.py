from django.shortcuts import render
from .models import Book, Chapter


def index(request):
    current_book = Book.objects.get(pk=1)
    chapter_list = Chapter.objects.filter(book__pk=1)
    context = {
        "book": current_book,
        "chapter_list": chapter_list,
    }
    return render(request, "books/index.html", context)


def read_chapter(request, chapter_number):
    chapter = Chapter.objects.get(chapter_number=chapter_number)
    chapter_content = chapter.content.splitlines()
    context = {"title": chapter.title, "content": chapter_content}
    return render(request, "books/chapter.html", context)
