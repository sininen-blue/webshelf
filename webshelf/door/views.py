from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import UserForm


def login_view(request):
    pass


def logout_view(request):
    pass


def register_view(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserForm()

    return render(request, "door/register.html", {"form": form})
