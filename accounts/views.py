from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def profile(request):
    return render(request, "accounts/profile.html")

def createProfile(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = UserCreationForm()
    return render(request,"accounts/createProfile.html" ,{"form":form})
