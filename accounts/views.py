from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

@login_required
def profile(request):
    return render(request, "accounts/profile.html")

def create_profile(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            p = Profile(user=user)
            p.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    context = {
        "form": form
    }
    return render(request,"accounts/create_profile.html", context)

