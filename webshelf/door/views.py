from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import LoginForm, RegisterForm
from desk.models import AuthorProfile


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/")
                # use the querystring returned by decorator
            else:
                context = {"form": LoginForm(), "error": "invalid credentials"}
                return render(request, "door/login.html", context)
    else:
        form = LoginForm()

    return render(request, "door/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            password_confirm = form.cleaned_data["password_confirm"]

            errors = []

            try:
                User.objects.get(username=username)
                errors.append("username already exists")
            except User.DoesNotExist:
                if password == password_confirm:
                    user = User.objects.create_user(
                        username, email=None, password=password
                    )
                    AuthorProfile.objects.create(user=user)

                    return HttpResponseRedirect("/")
                else:
                    errors.append("passwords do not match")

            context = {
                "form": RegisterForm(),
                "errors": errors,
            }

            return render(request, "door/register.html", context)
    else:
        form = RegisterForm()

    return render(request, "door/register.html", {"form": form})
