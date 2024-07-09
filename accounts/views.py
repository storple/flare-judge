from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect,render

from .models import Profile
from flare.shortcuts import htmx_render, htmx_redirect
from django_htmx.http import HttpResponseClientRedirect

def make_error_dict(form):
    fields = form.fields.keys()
    errors_dict = form.errors

    # dict containing all fields and their errors if they have any
    errors = {field : errors_dict.get(field,"") for field in fields}

    return errors.items()

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
            # this form has errors
            if request.htmx:
                # only send errors without full page reload and keep current form state
                errors = make_error_dict(form)

                context = {
                    "errors": errors
                }
                response = render(request,"accounts/errors.html",context)
                response.headers["HX-Reswap"] = "none"
                return response
            # if not htmx then do normal form rendering
    else:
        form = UserCreationForm()

    context = {
        "form": form,
    }
    return htmx_render(request,"accounts/create_profile.html",context)

@login_required
def logout_view(request):
    logout(request)
    # return htmx_redirect(request,reverse("login"))
    # full page load to update the profile dropdown / profile links
    return redirect(reverse("login"))

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            form.clean()
            user = form.get_user()
            if user is not None:
                login(request, user)
                # do a full redirect either way
                if request.htmx:
                    return HttpResponseClientRedirect(reverse("profile"))
                else:
                    return redirect(reverse("profile"))
            else:
                raise PermissionDenied
        else:
            # this form has errors
            if request.htmx:
                errors = {"all": "Your username and password didn't match. Please try again."}
                errors = errors.items()

                context = {
                    "errors": errors
                }
                response = render(request,"accounts/errors.html",context)
                response.headers["HX-Reswap"] = "none"
                return response
            # if not htmx then do normal form rendering
    else:
        form = AuthenticationForm()
    context = {
        "form": form
    }
    return htmx_render(request,"accounts/login.html",context)
