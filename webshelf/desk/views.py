from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models.query import EmptyQuerySet
from django.http import HttpResponseRedirect
from .forms import BookForm, ChapterForm
from books.models import Book, Chapter


def dashboard(request):
    current_author = User.objects.get(
        username=request.user.username).authorprofile

    context = {"book_list": Book.objects.filter(author=current_author)}
    return render(request, "desk/dashboard.html", context)


def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            user = User.objects.get(
                username=request.user.username).authorprofile
            new_book = form.save(commit=False)
            new_book.author = user
            new_book.save()
            return HttpResponseRedirect("/desk/")
    else:
        form = BookForm()

    return render(request, "desk/create_book.html", {"form": form})


def view_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    context = {
        "book": book,
    }
    return render(request, "desk/view_book.html", context)


def update_book(request):
    return render(request, "desk/dashboard.html")


def delete_book(request):
    return render(request, "desk/dashboard.html")


def create_chapter(request, book_id):
    book = Book.objects.get(pk=book_id)

    if request.method == "POST":
        form = ChapterForm(request.POST)
        if form.is_valid():
            new_chapter = form.save(commit=False)
            new_chapter.book = book

            new_chapter.chapter_number = set_chapter_number(book)

            new_chapter.save()
            return HttpResponseRedirect("/desk/")
    else:
        form = ChapterForm()

    context = {
        "form": form,
        "book": book,
    }

    return render(request, "desk/create_chapter.html", context)


def set_chapter_number(book):
    chapter_list = Chapter.objects.filter(book=book)

    if isinstance(chapter_list, EmptyQuerySet):
        return 1

    return len(chapter_list) + 1
