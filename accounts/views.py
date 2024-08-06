from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth import logout, login
from django.urls import reverse, reverse_lazy
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect,render

from .models import Profile
from flare.shortcuts import htmx_render, htmx_redirect, full_page_render
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
            url = reverse("login")
            url = "{}?signup=true".format(url)
            return htmx_redirect(request,url)
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

class ChangePasswordView(PasswordChangeView):
    template_name = "accounts/change_password.html"
    success_url = reverse_lazy("change_password_success")

def change_password_success_view(request):
    return full_page_render(request,"accounts/change_password_success.html")

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            form.clean()
            user = form.get_user()
            if user is None:
                raise PermissionDenied
            login(request, user)
            # do a full redirect either way
            default_url = reverse("profile")
            url = request.POST.get("next",default_url)

            if request.htmx:
                return HttpResponseClientRedirect(url)
            else:
                return redirect(url)
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

    from_signup = 'signup' in request.GET
    next = request.GET.get("next",None)

    context = {
        "form": form,
        "from_signup": from_signup,
        "next": next,
    }
    return htmx_render(request,"accounts/login.html",context)
