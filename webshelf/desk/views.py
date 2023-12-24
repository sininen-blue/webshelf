from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .forms import BookForm


def dashboard(request):
    return render(request, "desk/dashboard.html")


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


def view_book(request):
    return render(request, "desk/dashboard.html")


def update_book(request):
    return render(request, "desk/dashboard.html")


def delete_book(request):
    return render(request, "desk/dashboard.html")
