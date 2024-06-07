from django.contrib.auth.decorators import login_required
from django.urls import reverse

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile
from django.contrib.auth import logout, login
from flare.shortcuts import htmx_render, htmx_redirect

@login_required
def profile(request):
    return htmx_render(request,"accounts/profile.html")

def create_profile(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            p = Profile(user=user)
            p.save()
            return htmx_redirect(request,reverse("login"))
    else:
        form = UserCreationForm()
    context = {
        "form": form
    }
    return htmx_render(request,"accounts/create_profile.html",context)

@login_required
def logout_view(request):
    if request.method == "POST":
        logout(request)
    # logout(request)
    # when redirecting the context must be present, so we use the login view
    # however if its a POST then login_view is going to try to log the user in
    # this ensures it gets treated as a get request
    # request.method = "GET"
    # return login_view(request)
    return htmx_redirect(request,reverse("login"))
    # return htmx_render(request,"accounts/login.html")

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            form.clean()
            user = form.get_user()
            if user is not None:
                login(request, user)

                #changes request to be treated as a get request
                # request.method = "GET"
                # if request.htmx:
                # return profile(request)
                return htmx_redirect(request,reverse("profile"))
                # return htmx_render(request,"accounts/profile.html")
            else:
                #TODO: error handling
                pass
    else:
        form = AuthenticationForm()
    context = {
        "form": form
    }
    return htmx_render(request,"accounts/login.html",context)
