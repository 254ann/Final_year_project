from django.shortcuts import redirect, render
from accounts.forms import CustomUserCreationForm, UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib import messages


# Create your views here.

def loginPage(request):
    page = "login"

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "user does not exist")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "username or password does not exit")

    context = {"page": page}
    return render(request, "register.html", context)


def logoutUser(request):
    logout(request)
    return redirect("login")


def registerPage(request):
    form = CustomUserCreationForm()  # Use the custom form

    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data[
                "username"
            ]  
            user.save()
            login(request, user)
            messages.success(
                request, "Registration successful"
            )  
            return redirect("login")
        else:
            messages.error(request, "An error occurred during registration")
    context = {"form": form}
    return render(request, "register.html", context)
