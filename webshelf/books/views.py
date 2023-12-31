from django.shortcuts import render
from .models import Book, Chapter


def index(request, book_id):
    current_book = Book.objects.get(pk=book_id)
    chapter_list = Chapter.objects.filter(book__pk=book_id)
    context = {
        "book": current_book,
        "chapter_list": chapter_list,
    }
    return render(request, "books/index.html", context)


def read_chapter(request, book_id, chapter_number):
    book = Book.objects.get(pk=book_id)
    chapter_list = Chapter.objects.filter(book=book)
    chapter = chapter_list.get(chapter_number=chapter_number)

    chapter_content = chapter.content.splitlines()
    context = {
        "book": book,
        "chapter": chapter,
        "content": chapter_content,
        "last_chapter": len(chapter_list) + 1,
    }
    return render(request, "books/chapter.html", context)
